<template>
  <div>
    <b-table striped hover :items="items"></b-table>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  ready () {
    console.info('1')
    this.fetchData()
  },
  data () {
    console.info(this)
    this.$http.get('/stock')
      .success(function(res){
        console.info(res)
      })
      .error(function(err){
        console.info('err')
      });
    return {
      items: [
        { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
        { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
        { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
        { age: 38, first_name: 'Jami', last_name: 'Carney' }
      ]
    }
  },
  methods: {
    fetchData () {
      this.$http.get('/stock')
      .success(function(res){
        console.info(res)
      })
      .error(function(err){
        console.info('err')
      });
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
th {
  font-weight: normal;
}
</style>
