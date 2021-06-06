<template>
  <div class="search-card">
    <h3 class="card-title mb-4">Search Organisations</h3>
    <div class="search-buttons text-left mb-4">
      <a class="card-tab-btn mr-3" title="By keywords">By keywords</a>
      <a class="card-tab-btn active" title="By Job Title">By Job Title</a>
    </div>
    
    <!--  Search Field  -->
    <div class="input-group custom-input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text-custom" id="basic-addon1">@</span>
      </div>
      <input type="text"
             class="form-control"
             placeholder="e.g Ux Designer"
             aria-label="Username"
             aria-describedby="basic-addon1">
    </div>
    
    <!--  Country Dropdown  -->
    <div class="input-group custom-input-group mb-4">
      <div class="input-group-prepend">
        <span class="input-group-text-custom" id="basic-addon1">@</span>
      </div>
      <input type="text"
             class="form-control"
             placeholder="e.g Ux Designer"
             aria-label="Username"
             aria-describedby="basic-addon1">
    </div>
    
    <!--  Country  -->
    <div class="country-buttons text-left mb-4">
      <a class="card-tab-btn">North America</a>
      <a class="card-tab-btn active">APAC</a>
    </div>
    
    <div class="hr-seperator"></div>
    
    <!--  Score Seperator  -->
    <div class="score-section text-left">
      <span>Score:</span> <span class="score-number">0-60</span>
    </div>
    
    <!--  Range slider  -->
    <!-- <vue-slider v-model="value" :tooltip="'always'"/> -->
    
	<!--  Search Button  -->
    <button class="btn-search-lg text-white my-4" title="Search">Search</button>
    
    <!--  Popular Searches  -->
    <div class="popular-search-section text-left">
      <span class="popular-heading">Popular Searches: </span>
      <span class="popular-item">Director</span>, <span class="popular-item">Senior Web Developer</span>,
    </div>
    
  </div>
</template>

<script>
// import VueSlider from 'vue-slider-component'
// import 'vue-slider-component/theme/antd.css'

export default {
  data () {
    return {
      value: 60
    }
  },
  components: {
    // VueSlider
  },
  mounted() {
  
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.search-card{
  background: #FFFFFF;
  border-radius: 8px;
  padding: 40px;
}
.search-card .card-title{
  font-size: 20px;
  font-weight: 600;
  line-height: 25px;
  text-align: left;
}
.card-tab-btn{
  border: 1px solid #C6C6C6;
  box-sizing: border-box;
  border-radius: 8px;
  padding: 10px 20px;
  color: #374958;
  text-decoration: none;
  cursor: pointer;
}
.card-tab-btn.active{
  border: 1px solid #B3365B;
  background: #B3365B;
  color: #fff;
}
.input-group-text-custom{
  display: flex;
  align-items: center;
  padding: 0.75rem;
  margin-bottom: 0;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #495057;
  text-align: center;
  white-space: nowrap;
  border-radius: 0.25rem;
}
.custom-input-group{
  border: 1px solid #C6C6C6;
  border-radius: 8px;
}
.custom-input-group .form-control{
  border: 0 solid #C6C6C6;
  border-radius: 8px;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  padding: 1.5rem 0.75rem;
}
.custom-input-group .form-control:focus {
  box-shadow: none;
}
.country-buttons a{
  border-radius: 8px;
  margin-right: 8px;
  padding: 8px 16px;
  font-weight: 600;
  font-size: 12px;
  line-height: 15px;
}
.country-buttons a.active{
  background: rgba(179, 54, 91, 0.1);
  border: 1px solid rgba(179, 54, 91, 0.5);
  color: #B3365B;
}
.hr-seperator{
  border: 1px solid #C6C6C6;
  margin-top: 25px;
  margin-bottom: 15px;
}
.score-number{
  color: #B3365B;
}
.score-section{
  font-weight: 600;
  font-size: 14px;
  line-height: 18px;
}

.btn-search-lg{
  background: #B3365B;
  border-radius: 8px;
  padding: 0.75rem 60px;
  border: 0;
  line-height: 23px;
  width: 100%;
  font-size: 18px;
  font-style: normal;
  font-weight: 600;
  color: #E7E7E7;
}
/* Range slider css */
.vue-slider.vue-slider-ltr{
  margin-top: 35px;
}

.popular-heading,
.popular-item{
  font-size: 14px;
  line-height: 18px;
  color: #374958;
}
.popular-heading{
  font-weight: 600;
}
.popular-item{
  font-weight: 700;
  border-bottom: 1px solid #C6C6C6;
  cursor: pointer;
}
</style>
