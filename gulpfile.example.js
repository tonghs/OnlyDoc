var gulp = require('gulp');
    coffee = require('gulp-coffee'),
    plumber = require('gulp-plumber'),
    uglify = require('gulp-uglify'),
    minifyCSS = require('gulp-minify-css'),
    browserSync = require('browser-sync').create(),

    static_path = '#YOUR-STATIC-PATH#',
    coffee_path = static_path.concat('coffee/'),
    js_path = static_path.concat('js/'),
    css_path = static_path.concat('css/'),
    dist_path = static_path.concat('dist/')


// 编译coffee
gulp.task('coffee', function() {
    gulp.src(coffee_path.concat('**/*.coffee'))
        .pipe(plumber())
        .pipe(coffee())
        .pipe(gulp.dest(js_path));
});


// 自动刷新
gulp.task('browser-sync', function() {
    browserSync.init({
        notify: false,
        proxy: '51.tonghs.com',
        files: css_path + "**/*.css, " + js_path + "**/*.js, www/template/**/*.html"
    });
});

// 自动刷新
gulp.task('browser-sync-admin', function() {
    browserSync.init({
        notify: false,
        proxy: 'admin.tonghs.com',
        files: css_path + "**/*.css, " + js_path + "**/*.js, www/template/**/*.html"
    });
});

//压缩 css
gulp.task('minicss', function() {
    gulp.src(css_path.concat('**/*.css'))
    .pipe(minifyCSS())
    .pipe(gulp.dest(dist_path.concat('css')))
});

gulp.task('fonts', function() {
    gulp.src(css_path.concat('fonts/*.*'))
    .pipe(gulp.dest(dist_path.concat('css/fonts')))
});

//压缩 js
gulp.task('minijs', function() {
    gulp.src(js_path.concat('**/*.js'))
    .pipe(uglify())
    .pipe(gulp.dest(dist_path.concat('/js')))
});


// 默认任务
gulp.task('default', ['dev']);

gulp.task('dev', ['coffee', 'watch', 'browser-sync']);
gulp.task('admin', ['browser-sync-admin']);

gulp.task('online', ['coffee', 'minicss', 'fonts', 'minijs']);

// 监听 coffee
gulp.task('watch', function() {
    // 编译 coffee
    gulp.watch(coffee_path.concat('/**/*.coffee'), ['coffee']);
});
