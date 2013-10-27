'use strict';

angular.module('ng').directive('testElem', function () {
    return {
        restrict: 'A',
        templateUrl: '/HTML/partials/row.html',
        link: function (scope, iterStartElement, attr) {
            scope.data = [{date : "01-02-2013", title: "Random Wordddd", workdesc: "did this and this and thisddddddddddddddddddddddddddddddddddddddddddddddddddd", hours:"2" , cost: "tesaaaaaaaaaaaaastttt", paid:true}, 
            			   {date : "01-08-2013", title: "Random Work1", workdesc: "did this and this and this", hours:"2" , cost: "tesaaaaaaaaaaaaastttt", paid:false},
            			   {date : "01-09-2013", title: "Random Work2", workdesc: "did this and this and this", hours:"2" , cost: "tesaaaaaaaaaaaaastttt", paid:true}]
        }
    };
});



function FetchCtrl($scope, $http, $templateCache) {
  $scope.method = 'GET'; $scope.url = 'http://localhost:8888/works/EKS'; 
  $scope.fetch = function() {
    $scope.code = null;
    $scope.response = null;

    $http({method: $scope.method, url: $scope.url, cache: $templateCache}).
      success(function(data, status) {
        $scope.status = status;
        $scope.data = data;
        console.log(status);
      }).
      error(function(data, status) {
        $scope.data = data || "Request failed";
        $scope.status = status;
    });
  };      

    $scope.Test = function() {
    $scope.code = null;
    $scope.response = null;
    console.log($scope.data)

  };  
}