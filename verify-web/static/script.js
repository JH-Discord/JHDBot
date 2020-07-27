const app = new Vue({
	el: '#app',
	data: {
		//colors:[{id:0, hex:'#A82D80', disabled:false}, {id:1, hex:'#341347', disabled:false}],
		colors:[{id:0, hex:'#42275a', disabled:false}, {id:1, hex:'#734b6d', disabled:false}],
		id:2
	},
	computed: {
		gradient() {
			let colors = 'linear-gradient(45deg'
			this.colors.forEach(function(e){  
				colors += ',' + e.hex
			});
			colors += ')'
			return colors
		}
	}
})