angular.module('gosaccoApp')
   .controller('DepositCtrl', ['$scope', function($scope){
   	  var vm = this;
   	  vm.deposit = {};
   	  vm.depositFields = [
   	  {
            key: 'member',
            type: 'select',
            templateOptions: {
                label: 'Member Name',
                options:[
                {name:"Buhiire Keneth", value:"Buhiire Keneth"},
                {name:"Semakula Kraiba", value:"Semakula Kraiba"},
                {name:"Lubega Mark", value:"Lubega Mark"},
                {name:"Ricardo Mandela", value:"Ricardo Mark"}],
                placeholder:"Select a member",
                required: true
            }
        },
        {
            key: 'amount',
            type: 'input',
            templateOptions: {
                type: 'text',
                label: 'Amount',
                required: true
            }
   	  },
      {
            key:'date',
            type:'input',
            templateOptions:{
              type:'date',
              label:'Date',
              required:true
            }
      },
   	  {
   	  	    key:'saving_type',
   	  	    type:'select',
   	  	    templateOptions:{
   	  	    	label:"Savings Type",
   	  	    	options:[{name:"Savings", value:"Savings"},
   	  	    	{name:" Deposit", value:"Deposit"},
   	  	    	{name:"Short Term", value:"Short Term"}],
   	  	    	placeholder:"Select Savings Type",
   	  	    	required:true
   	  	    }
   	  }];
   }]);