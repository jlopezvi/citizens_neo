(function() {
    'use strict';

    angular.module('citizensNeoApp')
        .controller('LoginController', ['$timeout', '$http', '$location', '$auth', function($timeout, $http, $location, $auth) {
            var vm = this;

            vm.response = '';

            vm.authenticate = function (provider) {
                $auth.authenticate(provider);
            };

            vm.signInTwitter = function () {
                $http.post('/sign-in-twitter?callback=signInTwitter', {}).success(function (res) {
                    if (typeof res.auth_url !== 'undefined') {
                        var twitterWindow = window.open(res.auth_url);

                        var interval = window.setInterval(function() {
                            if (twitterWindow.closed) {
                                window.clearInterval(interval);

                                //$location.path('/home');
                                location.href='#/home';
                            }
                        }, 1000);
                    }
                });
            }
        }]);
})();
