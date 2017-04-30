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

desynovaApp.controller('desynovaCtrl', ['$scope', '$http', 'Notification', function ($scope, $http, Notification) {
    $scope.shortUrl = {
        original_url: ''
    }

    $scope.pasteLockly = {
        secret_key: '', 
        content: ''
    }

    $scope.shortUrlList = [];
    $scope.shareUrlList = [];
    $scope.niftyGainers = [];

    $scope.saveShortUrl = function() {
        if ($scope.shortUrl.original_url.length < 1){
            Notification.error("Please add url");
        }else{
            $http.post('/short_url/', $scope.shortUrl).
            success(function(data, status, headers, config) {
                getShortUrl();
                Notification.success(data.message);
            }).
            error(function(data, status, headers, config) {
                Notification.error(data.message);
            });
        }
    }
    var getShortUrl = function() {
        $http.get('/short_url/').
        success(function(data, status, headers, config) {
            $scope.shortUrlList = data.short_url_list;
        }).
        error(function(data, status, headers, config) {
            Notification.error(data.message);
        });
    }

    $scope.savePasteLockelyContent = function() {
        if ($scope.pasteLockly.secret_key.length < 1 || $scope.pasteLockly.content.length < 1){
            Notification.error("Please add secret_key and content");
        }else{
            $http.post('/paste_lockly/', $scope.pasteLockly).
            success(function(data, status, headers, config) {
                if (data.status){
                    getShareUrl();
                    Notification.success(data.message);
                }else{
                    Notification.error(data.message);
                }
            }).
            error(function(data, status, headers, config) {
                Notification.error(data.message);
            });
        }
    }
    var getShareUrl = function() {
        $http.get('/paste_lockly/').
        success(function(data, status, headers, config) {
            $scope.shareUrlList = data.share_url_list;
        }).
        error(function(data, status, headers, config) {
            Notification.error(data.message);
        });
    }

    var getNeseData = function() {
        $http.get('/get_neft_data/').
        success(function(data, status, headers, config) {
            $scope.niftyGainers = data.data;
        }).
        error(function(data, status, headers, config) {
            Notification.error(data.message);
        });
    }

    setInterval(function (){getNeseData();}, 3000*60);

    var init = function(){
        getShortUrl();
        getShareUrl();
        getNeseData();
    }

    init();
}]);