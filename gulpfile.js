
'use strict';
var gulp = require('gulp');
var gutil = require('gulp-util');
var del = require('del');
var uglify = require('gulp-uglify');
var gulpif = require('gulp-if');
var exec = require('gulp-exec');

var notify = require('gulp-notify');

var argv = require('yargs').argv;
// sass
var sass = require('gulp-sass');
var postcss = require('gulp-postcss');
var autoprefixer = require('autoprefixer');
var sourcemaps = require('gulp-sourcemaps');
// js
var watchify = require('watchify');
var browserify = require('browserify');
var vueify = require('vueify');
var babelify = require('babelify');
var source = require('vinyl-source-stream');
var rename = require('gulp-rename');
var es = require('event-stream');
// image optimization
var imagemin = require('gulp-imagemin');
// linting
var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');
// BrowserSync
var browserSync = require('browser-sync');

// gulp build --production
var production = !!argv.production;
// determine if we're doing a build
// and if so, bypass the livereload
var build = argv._.length ? argv._[0] === 'build' : false;
var watch = argv._.length ? argv._[0] === 'watch' : true;

// ----------------------------
// Error notification methods
// ----------------------------
var beep = function() {
  var os = require('os');
  var error = gulp.src('path/error.wav');
  if (os.platform() === 'linux') {
      // linux
      error.pipe(exec('aplay <%= file.path %>'));
  } else {
      // mac
      error.pipe(exec('afplay <%= file.path %>'));
  }
};
var handleError = function(task) {
  return function(err) {
    beep();

      notify.onError({
        message: task + ' failed, check the logs..',
        sound: false
      })(err);

    gutil.log(gutil.colors.bgRed(task + ' error:'), gutil.colors.red(err));
  };
};
// --------------------------
// CUSTOM TASK METHODS
// --------------------------
var tasks = {
  // --------------------------
  // Delete build folder
  // --------------------------
  clean: function(callback) {
    del(['static/build/']).then(function() {
      callback();
    });
  },
  // --------------------------
  // Copy static assets
  // --------------------------
  assets: function() {
    return gulp.src('./static/assets/**/*')
      .pipe(gulp.dest('static/build/assets/'));
  },
  // --------------------------
  // SASS (libsass)
  // --------------------------
  sass: function() {
    return gulp.src('./static/scss/*.scss')
      // sourcemaps + sass + error handling
      .pipe(gulpif(!production, sourcemaps.init()))
      .pipe(sass({
        sourceComments: !production,
        outputStyle: production ? 'compressed' : 'nested',
        includePaths: ['./node_modules/bootstrap-sass/assets/stylesheets']
      }))
      .on('error', handleError('SASS'))
      // generate .maps
      .pipe(gulpif(!production, sourcemaps.write({
        'includeContent': false,
        'sourceRoot': '.'
      })))
      // autoprefixer
      .pipe(gulpif(!production, sourcemaps.init({
        'loadMaps': true
      })))
      .pipe(postcss([autoprefixer({browsers: ['last 2 versions']})]))
      // we don't serve the source files
      // so include scss content inside the sourcemaps
      .pipe(sourcemaps.write({
        'includeContent': true
      }))
      // write sourcemaps to a specific directory
      // give it a file and save
      .pipe(gulp.dest('static/build/css'));
  },
  // --------------------------
  // Browserify
  // --------------------------
  // browserify: function() {
  //   var bundler = browserify('./static/js/index.js', {
  //     debug: !production,
  //     cache: {}
  //   });
  //   // determine if we're doing a build
  //   // and if so, bypass the livereload
  //   var build = argv._.length ? argv._[0] === 'build' : false;
  //   if (watch) {
  //     bundler = watchify(bundler);
  //   }
  //   var rebundle = function() {
  //     return bundler.bundle()
  //       .on('error', handleError('Browserify'))
  //       .pipe(source('build.js'))
  //       .pipe(gulpif(production, uglify()))
  //       .pipe(gulp.dest('static/build/js/'));
  //   };
  //   bundler.on('update', rebundle);
  //   return rebundle();
  // },

  browserify: function() {
    var files = [
      './static/vue/main.js',
      // './static/js/core.js',
    ]
    var steps = files.map(
      function(entry) {
        return browserify({ entries: [entry] })
            .transform(vueify)
            .transform(babelify)
            .bundle()
            .on('error', handleError('Browserify'))
            .pipe(source(entry))
            // rename them to have "bundle as postfix"
            .pipe(rename({
                dirname: '.',
                extname: '.bundle.js',
            }))
            .pipe(gulp.dest('static/build/js/'));
      }
    );
    // create a merged stream
    return es.merge.apply(null, steps);
  },

  // --------------------------
  // linting
  // --------------------------
  lintjs: function() {
    return gulp.src([
        'gulpfile.js',
        './static/js/index.js',
        './static/js/**/*.js'
      ]).pipe(jshint())
      .pipe(jshint.reporter(stylish))
      .on('error', function() {
        beep();
      });
  },
  // --------------------------
  // Optimize asset images
  // --------------------------
  optimize: function() {
    return gulp.src('./static/images/**/*.{gif,jpg,png,svg}')
      .pipe(imagemin({
        progressive: true,
        svgoPlugins: [{removeViewBox: false}],
        // png optimization
        optimizationLevel: production ? 3 : 1
      }))
      .pipe(gulp.dest('./static/images/'));
  },

};

gulp.task('browser-sync', function() {
    browserSync({
        port: process.env.PORT || 8080,
        proxy: "localhost:8000"
    });
});

gulp.task('reload-sass', ['sass'], function(){
  browserSync.reload();
});
gulp.task('reload-vue', ['browserify'], function(){
  browserSync.reload();
});

// --------------------------
// CUSTOMS TASKS
// --------------------------
gulp.task('clean', tasks.clean);
// for production we require the clean method on every individual task
var req = build ? ['clean'] : [];
// individual tasks
gulp.task('assets', req, tasks.assets);
gulp.task('sass', req, tasks.sass);
gulp.task('browserify', req, tasks.browserify);
gulp.task('lint:js', tasks.lintjs);
gulp.task('optimize', tasks.optimize);
gulp.task('test', tasks.test);

// --------------------------
// DEV/WATCH TASK
// --------------------------
// gulp.task('watch', ['assets', 'templates', 'sass', 'browserify', 'browser-sync'], function() {
  gulp.task('watch', ['assets', 'sass', 'browserify', 'browser-sync'], function() {

  // --------------------------
  // watch:sass
  // --------------------------
  gulp.watch('./static/scss/**/*.scss', ['reload-sass']);

  // --------------------------
  // watch:js
  // --------------------------
  gulp.watch('./static/vue/**/*.js', ['reload-vue']);
  gulp.watch('./static/vue/**/*.vue', ['reload-vue']);

  gutil.log(gutil.colors.bgGreen('Watching for changes...'));
});

// build task
gulp.task('build', [
  'clean',
  'assets',
  'sass',
  'browserify'
]);

gulp.task('default', ['watch']);

// gulp (watch) : for development and livereload
// gulp build : for a one off development build
// gulp build --production : for a minified production build
