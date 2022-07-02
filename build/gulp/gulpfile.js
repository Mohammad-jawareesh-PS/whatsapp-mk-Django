const { src, dest, watch, series } = require("gulp"),
  concat = require("gulp-concat"),
  sass = require("gulp-sass")(require("sass")),
  prefix = require("gulp-autoprefixer"),
  minify = require("gulp-clean-css"),
  terser = require("gulp-terser"),
  sourcemaps = require("gulp-sourcemaps");

// scss [main]
function compile_scss_main() {
  let folder_name = "main";
  return src(`../scss/${folder_name}/main.scss`)
    .pipe(sourcemaps.init())
    .pipe(sass())
    .pipe(prefix("last 2 versions"))
    .pipe(minify())
    .pipe(sourcemaps.write(`../../maps/css/${folder_name}`))
    .pipe(dest(`../../static/css/${folder_name}`));
}

// scss [login]
function compile_scss_login() {
  let folder_name = "login";
  return src(`../scss/${folder_name}/main.scss`)
    .pipe(sourcemaps.init())
    .pipe(sass())
    .pipe(prefix("last 2 versions"))
    .pipe(minify())
    .pipe(sourcemaps.write(`../../maps/css/${folder_name}`))
    .pipe(dest(`../../static/css/${folder_name}`));
}

// scss [sign_up]
function compile_scss_sign_up() {
  let folder_name = "sign_up";
  return src(`../scss/${folder_name}/main.scss`)
    .pipe(sourcemaps.init())
    .pipe(sass())
    .pipe(prefix("last 2 versions"))
    .pipe(minify())
    .pipe(sourcemaps.write(`../../maps/css/${folder_name}`))
    .pipe(dest(`../../static/css/${folder_name}`));
}

// scss [dashboard]
function compile_scss_dashboard() {
  let folder_name = "dashboard";
  return src(`../scss/${folder_name}/main.scss`)
    .pipe(sourcemaps.init())
    .pipe(sass())
    .pipe(prefix("last 2 versions"))
    .pipe(minify())
    .pipe(sourcemaps.write(`../../maps/css/${folder_name}`))
    .pipe(dest(`../../static/css/${folder_name}`));
}

// scss [message_engine]
function compile_scss_message_engine() {
  let folder_name = "message_engine";
  return src(`../scss/${folder_name}/main.scss`)
    .pipe(sourcemaps.init())
    .pipe(sass())
    .pipe(prefix("last 2 versions"))
    .pipe(minify())
    .pipe(sourcemaps.write(`../../maps/css/${folder_name}`))
    .pipe(dest(`../../static/css/${folder_name}`));
}

// scss [offers]
function compile_scss_offers() {
  let folder_name = "offers";
  return src(`../scss/${folder_name}/main.scss`)
    .pipe(sourcemaps.init())
    .pipe(sass())
    .pipe(prefix("last 2 versions"))
    .pipe(minify())
    .pipe(sourcemaps.write(`../../maps/css/${folder_name}`))
    .pipe(dest(`../../static/css/${folder_name}`));
}

//js [main]
function jsmin_main() {
  let folder_name = "main";
  return src(`../js/${folder_name}/*.js`)
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write(`../../maps/js/${folder_name}`))
    .pipe(dest(`../../static/js/${folder_name}`));
}

//js [login]
function jsmin_login() {
  let folder_name = "login";
  return src(`../js/${folder_name}/*.js`)
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write(`../../maps/js/${folder_name}`))
    .pipe(dest(`../../static/js/${folder_name}`));
}

//js [sign_up]
function jsmin_sign_up() {
  let folder_name = "sign_up";
  return src(`../js/${folder_name}/*.js`)
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write(`../../maps/js/${folder_name}`))
    .pipe(dest(`../../static/js/${folder_name}`));
}

//js [dashboard]
function jsmin_dashboard() {
  let folder_name = "dashboard";
  return src(`../js/${folder_name}/*.js`)
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write(`../../maps/js/${folder_name}`))
    .pipe(dest(`../../static/js/${folder_name}`));
}

//js [message_engine]
function jsmin_message_engine() {
  let folder_name = "message_engine";
  return src(`../js/${folder_name}/*.js`)
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write(`../../maps/js/${folder_name}`))
    .pipe(dest(`../../static/js/${folder_name}`));
}

//js [offers]
function jsmin_offers() {
  let folder_name = "offers";
  return src(`../js/${folder_name}/*.js`)
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write(`../../maps/js/${folder_name}`))
    .pipe(dest(`../../static/js/${folder_name}`));
}

// create watchtask
function watchTask() {
  // scss files
  watch("../scss/main/*.scss", compile_scss_main); // main
  watch("../scss/login/*.scss", compile_scss_login); // login
  watch("../scss/sign_up/*.scss", compile_scss_sign_up); // sign_up
  watch("../scss/dashboard/*.scss", compile_scss_dashboard); // dashboard
  watch("../scss/message_engine/*.scss", compile_scss_message_engine); // message_engine
  watch("../scss/offers/*.scss", compile_scss_offers); // offers

  // js files
  watch("../js/main/*.js", jsmin_main); // login
  watch("../js/login/*.js", jsmin_login); // login
  watch("../js/sign_up/*.js", jsmin_sign_up); // sign_up
  watch("../js/dashboard/*.js", jsmin_dashboard); // dashboard
  watch("../js/message_engine/*.js", jsmin_message_engine); // message_engine
  watch("../js/offers/*.js", jsmin_offers); // offers
}


// default gulp
exports.default = series(compile_scss_main, watchTask);
