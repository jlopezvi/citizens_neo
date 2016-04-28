/*global CitizensNeo, angular */

/**
 * @namespace CitizensNeo
 */
var CitizensNeo = angular.module('citizensNeoApp', ['ngRoute']);

CitizensNeo.config(function ($httpProvider, $routeProvider) {
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

    $httpProvider.defaults.transformRequest = function(obj) {
        var str = [];
        for (var p in obj) {
            str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        }

        return str.join("&");
    };

    $routeProvider
        .when('/login', {
            templateUrl: 'templates/login.html',
            controller: 'LoginController'
        })
        .when('/home', {
            templateUrl: 'templates/home.html',
            controller: 'HomeController'
        })
        .otherwise({redirectTo: '/login'});
});
