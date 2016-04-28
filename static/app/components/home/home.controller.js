(function () {
    'use strict';

    angular.module('citizensNeoApp')
        .controller('HomeController', ['$timeout', '$http', function($timeout, $http) {
            var vm = this;

            vm.users = [];

            $http.get('/getUsers').success(function (data) {
                if (angular.isDefined(data)) {
                    console.log(data);
                    // Init model data
                    vm.users = data;
                }
            });
        }]);
})();
