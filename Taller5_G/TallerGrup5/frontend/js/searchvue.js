import {axios} from './axios/lib/axios.js';

//const axios = require('./axios');
//node --experimental-modules index.mjs

new Vue({

		data:{

				fields:[

				{key:'tutulo', label:'Titulo'},
				{key: 'autores', label:'Autores'},
				{key:'isbn',label:'ISBN'},
				{key: 'calificacionprom', label:'Calificaciones'}

				], 

				libros:[],
		}, 
		methods:{
			getLibros: function(){
				const path = 'http://localhost:8000/api/libros/'
				axios.get(path).then((response)=> {
					this.libros = response.data;
				})
				.catch((error)=>{
					console.log(error)
				});
			}
		},
		created: function{
			this.getLibros();
		}
});
