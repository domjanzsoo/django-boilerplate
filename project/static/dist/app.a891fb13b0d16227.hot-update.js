"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(typeof self !== 'undefined' ? self : this)["webpackHotUpdatefrontend"]("app",{

/***/ "./src/services/HTTPClient.js":
/*!************************************!*\
  !*** ./src/services/HTTPClient.js ***!
  \************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   HTTPClient: function() { return /* binding */ clientInstance; }\n/* harmony export */ });\n/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! axios */ \"./node_modules/axios/lib/axios.js\");\n\nclass Client {\n  async getData(url, params = null) {\n    const resp = await axios__WEBPACK_IMPORTED_MODULE_0__[\"default\"].get('/api' + url, params);\n    console.log(resp);\n    return resp.data;\n  }\n}\nlet clientInstance = Object.freeze(new Client());\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvc2VydmljZXMvSFRUUENsaWVudC5qcyIsIm1hcHBpbmdzIjoiOzs7OztBQUFBO0FBRUE7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQSIsInNvdXJjZXMiOlsid2VicGFjazovL2Zyb250ZW5kLy4vc3JjL3NlcnZpY2VzL0hUVFBDbGllbnQuanM/MmM2YSJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgYXhpb3MgZnJvbSAnYXhpb3MnO1xyXG5cclxuY2xhc3MgQ2xpZW50IHtcclxuICAgIGFzeW5jIGdldERhdGEgKHVybCwgcGFyYW1zID0gbnVsbCkge1xyXG4gICAgICAgIGNvbnN0IHJlc3AgPSBhd2FpdCBheGlvcy5nZXQoJy9hcGknICsgdXJsLCBwYXJhbXMpO1xyXG5cclxuICAgICAgICBjb25zb2xlLmxvZyhyZXNwKTtcclxuICAgICAgICByZXR1cm4gcmVzcC5kYXRhO1xyXG4gICAgfVxyXG59XHJcblxyXG5sZXQgY2xpZW50SW5zdGFuY2UgPSBPYmplY3QuZnJlZXplKG5ldyBDbGllbnQoKSk7XHJcblxyXG5leHBvcnQgeyBjbGllbnRJbnN0YW5jZSBhcyBIVFRQQ2xpZW50IH07Il0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/services/HTTPClient.js\n");

/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "ca5f6c3711683590"; }
/******/ }();
/******/ 
/******/ }
);