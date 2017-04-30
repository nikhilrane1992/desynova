desynovaApp = angular.module('desynovaApp', ['angular-loading-bar', 'ui-notification'])
desynovaApp.config(['NotificationProvider', '$httpProvider', function(NotificationProvider, $httpProvider) {
    NotificationProvider.setOptions({
        delay: 3000,
        startTop: 20,
        startRight: 10,
        verticalSpacing: 20,
        horizontalSpacing: 20,
        positionX: 'right',
        positionY: 'top'
    });
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

desynovaApp.controller('desynovaCtrl', ['$scope', '$http', 'Notification', '$location', function ($scope, $http, Notification, $location) {

    $scope.pasteLockly = {
        secret_key: '', 
        share_url_id: $('#share_url_id').val()
    }

    $scope.getPasteLockelyContent = function() {
        $http.post('/decode_content/', $scope.pasteLockly).
        success(function(data, status, headers, config) {
            if (data.status){
                $scope.content = data.content;
            }else{
                Notification.error(data.message);
            }
        }).
        error(function(data, status, headers, config) {
            Notification.error(data.message);
        });
    }
}]);