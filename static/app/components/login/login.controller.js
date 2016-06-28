(function() {
    'use strict';

    angular.module('citizensNeoApp')
        .controller('LoginController', ['$timeout', '$http', function($timeout, $http) {
            var vm = this;

            vm.response = '';

            vm.signInTwitter = function () {
                $http.post('/sign-in-twitter', {}).success(function (res) {
                    if (typeof res.auth_url !== 'undefined') {
                        $http.jsonp(res.auth_url).success(function (response) {
                            vm.response = response;
                        });
                    }
                });
            }
        }]);
})();
