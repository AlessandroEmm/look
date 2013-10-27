'use strict'

document.app = angular.module('look', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{{').endSymbol('}}');
}).



    controller('work', function look($scope) {

        $scope.works =  [
            {date : "01-02-2013", title: "Random Wordddd", workdesc: "did this and this and thisddddddddddddddddddddddddddddddddddddddddddddddddddd", expenses: "Some LLLL", hours:"2" , cost: "tesaaaaaaaaaaaaastttt", paid:true, invoiceId:"EKS1"}, 
            {date : "01-08-2013", title: "Random Work1", workdesc: "did this and this and this", expenses: false, hours:"2" , cost: "tesaaaaaaaaaaaaastttt", paid:false, invoiceId:"EKS1"},
            {date : "01-09-2013", title: "Random Work2", workdesc: "did this and this and this" , expenses:"", hours:"2" , cost: "tesaaaaaaaaaaaaastttt", paid:true, invoiceId:"EKS1"}
        ];
        
        $scope.rowTemplate = ""

        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/works/EKS' , true);
        xhr.onload = function(e) {
            $scope.menuItems = this.response //JSON.parse(this.response);
            $scope.$apply()
        }


         
        $scope.init = function() {
            console.log($scope.works)
            xhr.send();

        };
       
    });

