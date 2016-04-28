(function() {
    'use strict';

    angular.module('citizensNeoApp')
        .controller('LoginController', ['$timeout', '$http', function($timeout, $http) {
            var vm = this;

            vm.username = '';
            vm.password = '';

            vm.post = function () {
                var data = $.param({
                    json: JSON.stringify({
                        username: vm.username,
                        password: vm.password
                    })
                });

                $http.post('/login', data).success(function (response) {

                });
            }
        }]);
})();
