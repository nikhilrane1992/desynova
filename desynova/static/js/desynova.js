desynovaApp = angular.module('desynovaApp', ['angular-loading-bar', 'ui-notification'])
desynovaApp.config(['NotificationProvider', function(NotificationProvider) {
    NotificationProvider.setOptions({
        delay: 3000,
        startTop: 20,
        startRight: 10,
        verticalSpacing: 20,
        horizontalSpacing: 20,
        positionX: 'right',
        positionY: 'top'
    });
}]);

desynovaApp.controller('desynovaCtrl', ['$scope', '$http', 'Notification', function ($scope, $http, Notification) {

}]);