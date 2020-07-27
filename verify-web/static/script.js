const app = new Vue({
	el: '#app',
	data: {
		//colors:[{id:0, hex:'#A82D80', disabled:false}, {id:1, hex:'#341347', disabled:false}],
		colors:[{id:0, hex:'#42275a', disabled:false}, {id:1, hex:'#734b6d', disabled:false}],
		id:2
	},
	methods: {
		addColor() {
			this.colors.push({id:this.id, hex:this.randomHex(), disabled:false})
			this.id++
			
		},
		removeColor() {
			if(this.colors[this.colors.length-1].disabled == false){
				if (this.colors.length > 2){
					this.colors.pop()
				}
			}

		},
		generateGradient(){
			for(let i=0;i<this.colors.length;i++){
				if (this.colors[i].disabled === false) this.colors[i].hex = this.randomHex()
			}
		},
		lockColor(index) {
			this.colors[index].disabled === true ?
				this.colors[index].disabled = false : 
				this.colors[index].disabled = true
		},
		randomHex() {
			return '#'+Math.random().toString(16).slice(2, 8)
		},
		up(index){
			if(index>0){
				let temp = this.colors[index]
				this.$set(this.colors,index,this.colors[index-1])
				this.$set(this.colors,index-1,temp)
			}
		},
		down(index){
			if(index<this.colors.length-1){
				let temp = this.colors[index]
				this.$set(this.colors,index,this.colors[index+1])
				this.$set(this.colors,index+1,temp)
			}
		}
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