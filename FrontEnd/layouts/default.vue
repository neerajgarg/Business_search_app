<template>
  <div>
    <!--  Header Section  -->
    <div class="main-header">
      <Header />
    </div>

    <!--  Slider Section  -->
    <div class="main-slider custom-bg">
      <div class="gradient-bg w-100">
        <div class="container header-text-fix">
          <div class="row justify-content-between align-items-center">
            <div class="col-md-7 my-2">
              <h1 class="header-title text-left text-white">
                Leading experts to
                find Organisations that<br>
                suits works
              </h1>
              <p class="text-white text-left sub-text">
                Logipsum provide affordable, high-quality organisation to suit your work and gives you boost to expand your wings.
              </p>
            </div>
            <div class="col-md-5 my-2">

              <div class="search-card">
                <h3 class="card-title mb-4">Search Organisations</h3>

                <!--Product being promoted  -->
                <div class="input-group custom-input-group mb-3">
                 <multiselect v-model="product" :options="products"
                    :multiple="false"
                    :close-on-select="true"
                    :clear-on-select="false"
                    :hideSelected="false"
                    :taggable="false"
                    placeholder="Product being promoted"
                    :preserve-search="true"
                    :internal-search="false"
                    @search-change="asyncFindProducts" >
                    <template slot="selection" slot-scope="{ values }">
                      <span class="multiselect__single" v-if="values.length">{{values[0]}}</span>
                    </template>
                    <template slot="option" slot-scope="props">
                      <div class="option__desc">
                        <span v-if="countries_value.includes(props.option)">
                          <input type="checkbox" value="" checked>
                        </span>
                        <span v-else> <input type="checkbox" value=""></span>
                        <span class="option__small">{{ props.option }}</span>
                      </div>
                    </template>
                    <template slot="selection">
                      <span class="mdi mdi-magnify"></span>
                    </template>
                  </multiselect>
                </div>

                <!--  Search Field  -->
                <div class="input-group custom-input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text-custom" id="basic-addon1">
                      <span class="mdi mdi-magnify"></span>
                    </span>
                  </div>
                  <input type="text" class="form-control" placeholder="e.g Ux Designer" aria-label="Username" v-model="keyword" aria-describedby="basic-addon1" required>
                </div>

                <!-- Category -->
                <div class="input-group custom-input-group mb-3 mag-icon-search">
                  <multiselect
                    v-model="category"
                    :options="categories"
                    :multiple="false"
                    :close-on-select="true"
                    :clear-on-select="false"
                    :hideSelected="false"
                    :taggable="false"
                    placeholder="Category"
                    :preserve-search="true" >
                    <template slot="selection" slot-scope="{ values, search, isOpen }">
                      <span class="multiselect__single" style="padding-left: 0px;" v-if="values.length">{{values[0]}}</span>
                    </template>
                    <span class="arrow" style="position: absolute; right: 0;margin:7px; font-size: 1.4rem;" slot="caret"><i class="mdi mdi-chevron-down"></i></span>
                  </multiselect>
                </div>
                <!-- asyncFindJobTitles -->
                <!-- Job title -->
                <div class="input-group custom-input-group mb-3 mag-icon-search">
                <!-- @search-change="getJobTitles" -->
                <multiselect
                    v-model="jobtitle"
                    
                    @search-change="asyncFindJobTitles" 
                    :options="jobtitles"
                    :multiple="false"
                    :close-on-select="true"
                    :clear-on-select="true"
                    :hideSelected="false"
                    :taggable="false"
                    placeholder="Job Title"
                    :internal-search="false"
                    :preserve-search="true"
                     >
                    <template slot="selection" slot-scope="{ values, search, isOpen }">
                      <span class="multiselect__single" style="padding-left: 0px;" v-if="values.length">{{values[0]}}</span>
                    </template>
                    <template slot="noOptions">{{jobSearchSlotText}}</template>
                    <template slot="noResult">{{jobSearchSlotText}}</template>
                    <template slot="spinner">Searching Please Wait...</template>
                    <span class="arrow" style="position: absolute; right: 0;margin:7px; font-size: 1.4rem;" slot="caret"><i class="mdi mdi-chevron-down"></i></span>
                  </multiselect>
                </div>
                <!-- Country Selection -->
                <div class="country">
                 <multiselect
                    v-model="country"
                    :options="countries"
                    :multiple="true"
                    :internal-search="false"
                    :close-on-select="false"
                    :clear-on-select="false"
                    :hideSelected="false"
                    :taggable="false"
                    placeholder="Any Country"
                    :preserve-search="true"
                    @search-change="asyncFind" >
                    <template slot="selection" slot-scope="{ values }">
                      <span class="multiselect__single" v-if="values.length">{{values[0]}}</span>
                    </template>
                    <template
                      slot="option"
                      slot-scope="props">
                      <div class="option__desc">
                        <span v-if="countries_value.includes(props.option)">
                          <input type="checkbox" value="" checked>
                        </span>
                        <span v-else>
                          <input type="checkbox" value="">
                        </span>
                        <span class="option__small">{{ props.option }}</span>
                      </div>
                    </template>
                    <template slot="selection">
                      <span class="mdi mdi-magnify"></span>
                    </template>
                  </multiselect>
                </div>

                <!--  Country  -->
                <div class="country-buttons text-left my-4" >
                  <a class="card-tab-btn" v-on:click="showCountry(selectedCountry)" :class="selectedCountryGroup == selectedCountry ? 'active' : ''" :key="index" v-for="selectedCountry, index in country_groups">{{selectedCountry}}</a>
                  <!-- <a class="card-tab-btn active">APAC</a> -->
                 <div id="show-city" class="show-city mt-3" v-if="isHidden == true">
                      <!-- <div class="close-city">
                          <a class="btn-dark " v-on:click="isHidden = false">x</a>
                      </div> -->
                      <div class="city-list">
                          <a class="card-tab-btn " @click="removeCountry(city)" :key="index" v-for="city, index in countrylist">
                            {{city}} 
                            <span v-if="!country_selected.includes(city)" class="mdi mdi-check-bold ml-2"></span>
                          </a>
                      </div>
                </div>
                </div>

                <!--  Search Button  -->
                <!-- for disabling search if search filed is empty use :disabled="keyword.trim() == ''" -->
                <button class="btn-search-lg text-white my-4" type="button" data-toggle="button" @click="search"  :disabled="keyword.trim() == ''" title="Search" >Search</button>
                <!--  Popular Searches  -->
                <!-- <div class="popular-search-section text-left"   v-if="keywords.length > 0">
                  <span class="popular-heading">Popular Searches: </span>
                  <span class="popular-item" v-for="(keyword, i) in keywords" :key="i">
                      <a @click="search_keyord(keyword)">{{ keyword }}</a>,
                    </span>
                </div> -->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!--  Bottom Section  -->
    <div v-if="isSearchDone" class="bottom-section">

      <!--  Filter Section  -->
      <div class="filter-section mb-4">
        <div class="container">
          <div class="main-filter-section">
            <div class="form-row">
              <div class="form-group col-md-2 text-left">
                <label class="typo__label">State</label>
                <!-- <select
                  v-model="state"
                  class="text-capitalize form-control w-100"
                  @change="searchByState"
                >
                  <option :value="state" v-for="state, index in states" :key="index">
                    {{ state }}
                  </option>
                </select> -->
                <multiselect
                  v-model="state"
                  :options="states"
                  :multiple="false"
                  :preselect-first="true"
                  placeholder="Any"
                  :close-on-select="true"
                  @input="searchByState"

                  :clear-on-select="false"
                  :preserve-search="true" >

                  <template slot="selection"
                            slot-scope="{ values, search, isOpen }">
                    <span class="multiselect__single" v-if="values.length">{{values.join(', ')}}</span>
                  </template>
                  <template slot="option" slot-scope="props">
                    <div class="option__desc">
                      <span class="option__small" v-html="props.option"></span>
                    </div>
                  </template>
                </multiselect>
                
              </div>
              <div class="form-group col-md-3 text-left">
                <label class="typo__label">City</label>
                <!-- <select
                  v-model="city"
                  class="text-capitalize form-control w-100"
                  @change="searchByCity"
                  :disabled="!state || state == 'any'"
                >
                  <option :value="city" v-for="city, index in cities" :key="index">
                    {{ city }}
                  </option>
                </select> -->
                <multiselect
                  v-model="city"
                  :options="cities"
                  :multiple="false"
                  :preselect-first="true"
                  placeholder="Any"
                  :close-on-select="true"
                  @input="searchByCity"
                  :clear-on-select="false"
                  :preserve-search="true" >

                  <template slot="selection"
                            slot-scope="{ values, search, isOpen }">
                    <span class="multiselect__single" v-if="values.length">{{values.join(', ')}}</span>
                  </template>
                  <template slot="option" slot-scope="props">
                    <div class="option__desc">
                      <span class="option__small" v-html="props.option"></span>
                    </div>
                  </template>
                </multiselect>

              </div>

              <div class="form-group col-md-3 text-left">
                <label class="typo__label">Company Size</label>
                <multiselect
                  v-model="employee"
                  :options="company_size"
                  :multiple="true"
                  :preselect-first="true"
                  placeholder="Any"
                  :close-on-select="false"
                  @input="search"
                  :clear-on-select="false"
                  :preserve-search="true" >

                  <template slot="selection"
                            slot-scope="{ values, search, isOpen }">
                    <span class="multiselect__single" v-if="values.length">{{values.join(', ')}}</span>
                  </template>
                  <template slot="option" slot-scope="props">
                    <div class="option__desc">
                      <span v-if="comapny_value.includes(props.option)">
                        <input type="checkbox" value="" checked>
                      </span>
                      <span v-else>
                        <input type="checkbox" value="">
                      </span>
                      <span class="option__small" v-html="props.option"></span>
                    </div>
                  </template>
                </multiselect>
              </div>
              <div class="form-group col-md-2"></div>
              <div class="form-group col-md-2 text-left">
                <label for="inputPages">Records</label>
                <!-- <select
                  id="page_pl"
                  class="form-control"
                  v-model="rpp"
                  @change="searchBySize"
                >
                  <option value="15">15</option>
                  <option value="50">50</option>
                  <option value="80">80</option>
                  <option value="100">100</option>
                </select> -->
                <multiselect
                  v-model="rpp"
                  :options="record_options"
                  :multiple="false"
                  :preselect-first="true"
                  placeholder="Any"
                  :close-on-select="true"
                  @input="search"
                  :clear-on-select="false"
                  :preserve-search="true" >

                  <template slot="selection"
                            slot-scope="{ values, search, isOpen }">
                    <span class="multiselect__single" v-if="values.length">{{values.join(', ')}}</span>
                  </template>
                  <template slot="option" slot-scope="props">
                  </template>
                </multiselect>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!--  Keep walking  -->
      <div v-if="isSearchDone" class="keep-walking-section mb-4">
        <div class="container">
          <p class="keep-walking mb-0 text-white">Keep Walking</p>
          <p class="you-are-gem mb-0 text-white">You are the Gem</p>
        </div>
      </div>

      <!--  Card Section  -->
      <div v-if="isSearchDone" class="filter-cards-section" >
        <Filtercards :companies="companies" />
      </div>

      <!--  Show More button  -->
      <button v-if="isSearchDone && companies && companies.length > 0 "  @click="fetchMore" class="btn-show-more text-white">Show more</button>
      
      <div class="text-center text-white" v-else>No Records found</div>

      <!--  Most View Section  -->
      <div v-if="isSearchDone" class="most-viewed-organisation">
        <div class="container mt-5 mb-4">
          <p class="most-viewed-heading mb-0 text-white">Most viewed organisation for </p>
          <p class="most-viewed-term mb-0 text-white">
            {{ keyword }}
            <!-- UX Designer -->
          </p>
        </div>

        <!--   Cards   -->
        <div  v-if="isSearchDone" class="filter-cards-section">
          <Filtercards  :companies="popular"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Header from '../components/Header';
  import Homeslider from '../components/homeSlider'
  import Filtersection from '../components/Filtersection'
  import Filtercards from '../components/Filtercards'
  import constants from "../api/constants"
  import Multiselect from 'vue-multiselect'

  var VueScrollTo = require("vue-scrollto");
  export default {
    components: {
      Header,
      Homeslider,
      Filtersection,
      Filtercards,
      Multiselect
    },
    data() {
      return {
        category : '',
        categories : [],

        jobtitle: '',
        jobtitles: [],
        jobSearchSlotText: 'Loading please Wait . . .',

        showModal: false,
        isSearching: false,
        countrylist: [],
        country_groups:[],
        country_selected: [],
        selectedCountryGroup: [],
        isHidden: false,
        page:1,
        scrollPosition: 0,
        view: "list",
        sliderMin: 0,
        sliderMax: 100,
        sliderVal: 80,
        sliderPos: null,
        isSearchDone: false,
        hasEqualSize: false,
        isSubscribed: false,
        isStateSelected: false,

        countries: constants.COUNTRIES,
        states: [""],
        cities: [""],
        emps: ["any"],
        companies: [],
        products:constants.PRODUCTS,
        popular: [],
        keywords: [],
        flips: [],
        popflips: [],
        last_id: null,

        type: "keyword",
        rpp:15,
        country: [],
        product:[],
        
        state: "All",
        city: "All",
        keyword: "",
        employee: "Any",
        countries_value:[],
        comapny_value:[],
        company_size: [
          'Any', '1-99', '100-249', '250-499', '500-999', '1000-4999', '5000-9999', '10000+'
        ],
        record_options: [
          '15', '50', '80', '100'
        ]

      };
    },
    created() {
      this.getKeywords();
      this.updateValues();
      this.loadCountryGroups();
      this.loadCategories();
      this.getJobTitles();
    },
    watch: {
      sliderVal(newVal) {
        const chngedVal = Number(
          ((newVal - this.sliderMin) * 100) / (this.sliderMax - this.sliderMin)
        );
        this.sliderPos =
          this.sliderVal == 0
            ? `0px`
            : `calc(${chngedVal}% + (${3 - chngedVal * 0.15}px))`;
      },
    },
    mounted() {
      window.addEventListener("scroll", this.updateScroll);
    },
    methods: {
      updateScroll() {
        this.scrollPosition = window.scrollY;
      },
      async asyncFindJobTitles(query){
        var filter= []
        console.log(query.toLowerCase())
        await this.jobtitles.forEach(job=>{
          if(job.toLowerCase().startsWith(query.toLowerCase())){
            filter.push(job)
          }
        })
        this.jobtitles=filter
      },
      async asyncFindProducts(query){
        var filter= []
        await constants.PRODUCTS.forEach(product=>{
          if(product.toLowerCase().startsWith(query.toLowerCase())){
            filter.push(product)
          }
        })
        this.products=filter
      },
      async asyncFind(query) {
        var filter= []
        await constants.COUNTRIES.forEach(country=>{
          if(country.toLowerCase().startsWith(query.toLowerCase())){
            filter.push(country)
          }
        })
        this.countries=filter
      },
      async showCountry(selectedCountry){
        if(this.selectedCountryGroup.includes(selectedCountry)){
         var index = this.selectedCountryGroup.indexOf(selectedCountry);
          if (index > -1) {
              this.selectedCountryGroup.splice(index, 1);
              this.isHidden = false;
          }
        }else{
          this.selectedCountryGroup.push(selectedCountry);
          this.isHidden = true;
          const res = await this.$axios.$get("/group?country_group="+selectedCountry);
          if(res.status == 'success'){
            this.countrylist = res.Countries
          }
        }
      },
      async getJobTitles(query){
        let res = await this.$axios.$get("/jobtitle");
        this.jobtitles= res.Titles;
      },

      async loadCountryGroups(){
          const res = await this.$axios.$get("/listgroups");
          if(res.status == "success"){
            this.country_groups= res.data;
            console.log(res.data);
          }
      },
      async loadCategories(){
        const res = await this.$axios.$get("/category");
        if(res.status == "success"){
          this.categories= res.Categories;
        }
      },
      removeCountry(city){
          const index = this.country_selected.indexOf(city);
          if (index > -1) {
            this.country_selected.splice(index, 1);
          }else{
            this.country_selected.push(city);
          }
      },

      removeFromSearch(){
        this.country = this.countrylist.filter((item)=>{
            return !this.country_selected.includes(item)
        })
      },

      scrollToTop() {
        window.scrollTo(0, 0);
      },

      toogleMenu() {
        var menu = document.getElementById("main-navbar");
        menu.classList.toggle("is-active");
      },

      toggleFlip(i) {
        if (this.flips.includes(i)) {
          const indx = this.flips.indexOf(i);
          this.flips.splice(indx, 1);
        } else {
          this.flips.push(i);
          this.addPopularity(this.companies[i].id);
        }
      },

      togglePopFlip(i) {
        if (this.popflips.includes(i)) {
          const indx = this.popflips.indexOf(i);
          this.popflips.splice(indx, 1);
        } else {
          this.popflips.push(i);
        }
      },

      search_keyord(kywrd) {
        this.keyword = kywrd;
        this.search_type = "keyword";
        this.search();
      },

      compare(a, b) {
        // Use toUpperCase() to ignore character casing
        const A = a.score;
        const B = b.score;

        let comparison = 0;
        if (A > B) {
          comparison = -1;
        } else if (A < B) {
          comparison = 1;
        }
        return comparison;
      },

      applyFilter() {
        this.isSearching = true;
        this.showModal = false;
        this.searchBySize();
      },

      updateValues() {
        const chngedVal = Number(
          ((this.sliderVal - this.sliderMin) * 100) /
          (this.sliderMax - this.sliderMin)
        );
        this.sliderPos =
          this.sliderVal == 0
            ? `0px`
            : `calc(${chngedVal}% + (${3 - chngedVal * 0.15}px))`;
      },

      async addPopularity(id) {
        await this.$axios.$post("/add_popularity", {
          id,
        });
      },

      async search() {
        //intial search filter to retrive the companies from the backend
        this.isSearchDone = true;
        this.isSearching = true;  
        this.page = 1;
        //search box parameters
         let params = {
          score: this.sliderVal,
          keyword: this.keyword,
          search_type: this.type,
          country: this.country !== "any" ? this.country : "",
          state:  this.state !== "All" ? this.state : "",
          city: this.city !== "All" ? this.city : "",
          employee: !this.employee.includes("Any") ? this.employee : "1-10000000",
          category: this.category,
          jobtitle: this.jobtitle,
        };
        console.log(params)
        //post the parameters to /search api endpoint to retrive the filterd list of comapnies
        let url = "/search?limit="+this.rpp+"&page="+this.page
        const res = await this.$axios.$post(url,  params );

        // if we get the data succefully check number of companies to update the last_id var and 
        //comapnies list to be filled with retrived data
        if (res.status == 'sucess') {
          if (res.data.length > 0) {
            this.last_id = res.data[res.data.length - 1].id;
          }
          this.companies = res.data;
        }

        //once the backend api response is recived user will be scrolled to a results
        this.isSearching = false;
        VueScrollTo.scrollTo("#results", 200, { offset: -50 });
        
        //popularResult list will be populated with according results of the keyword being searched
         params = {
          keyword: this.keyword,
          search_type: this.type,
        };
        const popularResult = await this.$axios.$get("/popular", { params });
        //if successful popular list will be populated
        if (popularResult.status == 'sucess') {
          this.popular = popularResult.data;
        }

        //if the user input for the country is any then the subfilter of state and city will be filled with all the available cities and states
        if (this.country == "any") {
          const states = await this.$axios.$post("/states");
          const cities = await this.$axios.$get("/cities"); 
          this.states = states.data;
          this.cities = cities.data;
        } 
        //if user has particular country then that countries sates and cities will be populated
        else {
          let params = { country: this.country };
           this.$axios.$post("/states",  params ).then((response)=>{
              this.states = response.data;
          });
          const cities = await this.$axios.$get("/cities",  params );
          this.cities = cities.data;
        }
        this.hasEqualSize = res.data.length == this.rpp ? true : false;
      },
      async searchBySize() {
        this.isSearching = true;
        this.removeFromSearch();
        this.page = 1;
        let url = "/search?limit="+this.rpp+"&page="+this.page
        const res = await this.$axios.$post(url, 
           {
            score: this.sliderVal,
            limit: this.rpp,
            page: this.page,
            keyword: this.keyword,
            search_type: this.type,
            country: this.country !== "any" ? this.country : "",
            state:  this.state !== "All" ? this.state : "",
            city: this.city !== "All" ? this.city : "",
            employee: !this.employee.includes("Any") ? this.employee : "1-10000000",
            category: this.category,
            jobtitle: this.jobtitle,
        });
        if (res.status == 'sucess') {
          if (res.data.length > 0) {
            this.last_id = res.data[res.data.length - 1].id;
          }

          this.companies = res.data.sort(this.compare);
        }

        this.hasEqualSize = res.data.length == this.rpp ? true : false;
        this.isSearching = false;
      },

      async searchByState() {
        console.log('asfdadsf')
        this.isSearching = true;
        this.page = 1;
        this.removeFromSearch();
        let url = "/search?limit="+this.rpp+"&page="+this.page
          const res = await this.$axios.$post(url, 
           {
            score: this.sliderVal,
            keyword: this.keyword,
            search_type: this.type,
            country: this.country !== "any" ? this.country : "",
            state:  this.state !== "All" ? this.state : "",
            city:  this.city !== "All" ? this.city : "",
            employee: !this.employee.includes("Any") ? this.employee : "1-10000000",
            category: this.category,
            jobtitle: this.jobtitle,
          },
        );

        if (res.status == 'sucess') {
          if (res.data.length > 0) {
            this.last_id = res.data[res.data.length - 1].id;
          }
          this.companies = res.data.sort(this.compare);
        }

        const cities = await this.$axios.$get("/cities", {
          params: { state: this.state !== "any" ? this.state : "" },
        });

        this.cities = cities.data;
        this.cities.push("All");

        this.city = "All";

        this.hasEqualSize = res.data.length == this.rpp ? true : false;
        this.isSearching = false;
      },

      async searchByCity() {
        this.isSearching = true;
        this.removeFromSearch();
        this.page = 1;
         let url = "/search?limit="+this.rpp+"&page="+this.page
          let param = {
            score: this.sliderVal,
            limit: this.rpp,
            page:this.page,
            keyword: this.keyword,
            search_type: this.type,
            state:  this.state !== "All" ? this.state : "",
            city:  this.city !== "All" ? this.city : "",
            employee: !this.employee.includes("Any") ? this.employee : "1-10000000",
            category: this.category,
            jobtitle: this.jobtitle,
          }

        const res = await this.$axios.$post(url, param);

        if (res.status == 'sucess') {
          if (res.data.length > 0) {
            this.last_id = res.data[res.data.length - 1].id;
          }
          this.companies = res.data.sort(this.compare);
        }

        this.hasEqualSize = res.data.length == this.rpp ? true : false;
        this.isSearching = false;
      },

      async fetchMore() {
        this.isSearching = true;
        this.removeFromSearch();
        this.page = this.page + 1;
         let url = "/search?limit="+this.rpp+"&page="+this.page
     
          let param = {
            lId: this.last_id,
            score: this.sliderVal,
            limit: this.rpp,
            keyword: this.keyword,
            search_type: this.type,
            country: this.country !== "any" ? this.country : "",
            state:  this.state !== "All" ? this.state : "",
            city: this.city !== "All"  ? this.city : "",
            employee: !this.employee.includes("Any") ? this.employee : "1-10000000",
            category: this.category,
            jobtitle: this.jobtitle,
          }

        const res = await this.$axios.$post(url, param);

        if (res.status == 'sucess') {
         
          if (res.data.length > 0) {
            this.last_id = res.data[res.data.length - 1].id;
            res.data.sort(this.compare).forEach((el) => this.companies.push(el));
          }
        }

        this.hasEqualSize = res.data.length == this.rpp ? true : false;
        this.isSearching = false;
      },

      async getKeywords() {
        const res = await this.$axios.$get("/keywords");
        this.keywords = res.data;
      },

      getClass(score){
        if(score <=35){
          return 'is-critical'
        } else if(score >35 && score <= 60){
          return 'is-good'
        } else{
          return ''
        }

      }
    },
  }
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .main-header nav.navbar{
    position: absolute;
    width: 100%;
  }
  .main-slider{
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .main-slider.custom-bg {
    background: url(./../assets/img/bg-image.jpg);
    background-size: cover;
    background-position: top;
  }
  .gradient-bg{
    background: linear-gradient(246.04deg, #031C32 22.45%, rgba(255, 0, 0, 0.3) 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-size: cover;
    background-position: 100% 100%;
  }
  .keep-walking{
    font-size: 24px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px;
    letter-spacing: 0em;
    text-align: left;
  }
  .you-are-gem{
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: 20px;
    letter-spacing: 0em;
    text-align: left;
  }

  .btn-show-more{
    background: #B3365B;
    border-radius: 8px;
    padding: 10px 60px;
    border: 0;
    font-size: 18px;
    font-weight: 700;
    line-height: 23px;
  }
  .most-viewed-heading{
    font-size: 24px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px;
    text-align: center;
  }
  .most-viewed-term{
    font-size: 24px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px;
    text-align: center;
    color: #EBCACA !important;
  }
  .bottom-section{
    padding-top: 80px;
    padding-bottom: 80px;
  }
  .header-title{
    font-size: 48px;
    font-style: normal;
    font-weight: 800;
    line-height: 58px;
    letter-spacing: 0em;
    text-align: left;
  }
  .sub-text{
    font-size: 20px;
    font-style: normal;
    font-weight: 400;
    line-height: 30px;
    letter-spacing: 0em;
    text-align: left;
  }

  body {
    font-family: Mulish;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    background: #031C32;
  }

  /*search css start */
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
    display: inline-block;
    border: 1px solid #C6C6C6;
    box-sizing: border-box;
    border-radius: 8px;
    padding: 10px 20px;
    color: #374958;
    text-decoration: none;
    cursor: pointer;
  }
  .card-tab-btn:hover{
    text-decoration: none;
    color: #374958;
  }
  .card-tab-btn.active{
    border: 1px solid #B3365B;
    background: #B3365B;
    color: #fff;
  }
  .input-group-text-custom{
    display: flex;
    align-items: center;
    padding: 5px 0 0 12px;
    margin-bottom: 0;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #495057;
    text-align: center;
    white-space: nowrap;
    border-radius: 0.25rem;
  }
  .input-group-text-custom .mdi.mdi-magnify{
    font-size: 26px;
  }
  .custom-input-group{
    border-radius: 8px;
  }
  .custom-input-group .form-control{
    border-radius: 8px !important;
    padding: 1.5rem 0.75rem;
    padding-left: 45px;
    color: #374958 !important;
  }
  .custom-input-group .form-control:focus {
    box-shadow: none;
  }
  .country-buttons a{
    border-radius: 10px;
    margin-right: 4px;
    padding: 8px 16px;
    font-weight: 600;
    font-size: 12px;
    line-height: 15px;
    display: inline-block;
  }
  .country-buttons a.active{
    background: rgba(179, 54, 91, 0.1);
    border: 1px solid rgba(179, 54, 91, 0.5);
    color: #B3365B;
  }
  .hr-seperator{
    border: 1px solid #C6C6C6;
    margin-top: 20px;
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

  .btn-search-lg:active{
            transform: scale(0.98);
            /* Scaling button to 0.98 to its original size */
            box-shadow: 3px 2px 22px 1px rgba(0, 0, 0, 0.24);
            /* Lowering the shadow */
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
    cursor: pointer;
  }
  .popular-item a{
    border-bottom: 1px solid #C6C6C6;
  }
  /* End search css */

  /* start of heder css */
  .navbar-brand{
    font-size: 32px;
    font-weight: 700;
    line-height: 38px;
    text-align: left;
  }
  .nav-item a{
    font-size: 16px;
    font-weight: 600;
    line-height: 20px;
    text-align: left;
    color: #fff;
  }
 
  nav.navbar{
    position: absolute;
    width: 100%;
  }
  /* End of header css */

  .bottom-section{
    text-align: center;
  }

  /* Filter Section */
  .main-filter-section{
    background: #B3365B;
    border-radius: 8px;
    padding: 32px;
  }
  .main-filter-section select{
    background: #EBCACA;
    border-radius: 8px;
    padding: 5px;
    height: 45px;
  }

  .main-filter-section .form-group label{
    font-size: 16px;
    font-weight: 600;
    line-height: 20px;
    color: #C6C6C6 !important;
  }

  /* Vue slider START */
  .vue-slider-process {
    background-color: #B3365B !important;
  }
  .vue-slider-dot-handle {
    border: 2px solid #B3365B;
    transition: box-shadow 0.3s, border-color 0.3s;
  }
  .vue-slider-dot-handle:hover,
  .vue-slider:hover .vue-slider-dot-handle,
  .vue-slider:hover .vue-slider-dot-handle:hover,
  .vue-slider:hover .vue-slider-process{
    border-color: #B3365B !important;
  }
  .vue-slider-dot-handle-focus{
    box-shadow: 0 0 0 0 !important;
  }
  .vue-slider-dot{
    width: 11px !important;
    height: 11px !important;
    cursor: pointer;
  }
  .vue-slider-dot-tooltip-inner {
    border-radius: 16px 16px;
    border-color: #B3365B !important;
    background-color: #B3365B !important;
    font-size: 12px;
    width: 30px;
    height: 26px;
    padding: 4px 0 0 0;
  }
  .vue-slider-dot-tooltip-inner-top::after {
    top: 89%;
    left: 50.4%;
    border-width: 10px;
  }
  /* Vue slider END */

  /* multiselect dropdown */
  .multiselect__element:hover{
    background-color: #EBCACA !important;
    color: #B3365B  !important;
  }

  .multiselect__option--highlight {
    background: #EBCACA  !important;
    outline: none;
    color: #B3365B  !important;
  }

  .multiselect__option--highlight::after {
    background: #EBCACA  !important;
    content: none;
    color: #B3365B  !important;
  }
  .multiselect__option--selected{
    content: none;
    background: #EBCACA;
    
  }

  .multiselect__input::before{
    background: olivedrab;
  }

  ::-webkit-scrollbar{
    width: 5px;
    height: 5px;
    border-radius: 8px;
  }
  /* Track  */
  ::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
  } 

  /* Handle  */
  ::-webkit-scrollbar-thumb {
    background: #ff3377;
    width: 5px;
    height: 45px;
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.5);
  }

  /* ::-webkit-scrollbar-thumb:window-inactive {
    background: #ff3377;
    width: 5px;
    height: 40px;
  } */

  input[type=checkbox] {
    border: 1px solid #B3365B;
    outline: 1px solid #B3365B;
    box-sizing: border-box;
    border-radius: 2px;
    background: #B3365B;
    outline-style: auto;
  }

  input:checked{
    color: #B3365B;
    background-color: green !important;
    background: green !important;
    background: #B3365B;
  }

  .search-card .input-group.custom-input-group .input-group-prepend{
    position: absolute;
    z-index: 5;
  }
  .search-card .input-group.custom-input-group .form-control:focus{
    border-color: #B3365B !important;
  }
  .multiselect__tags {
    padding: 10px 40px 3px 12px !important;
    min-height: 48px;
    border-radius: 8px !important;
    border: 1px solid #ced4da !important;
  }
  .multiselect__input, .multiselect__single{
    border-radius: 8px !important;
    line-height: 24px;
    /* padding: 0 0 0 32px; */
  }
  .country .multiselect__input,.country .multiselect__single{
    border-radius: 8px !important;
    line-height: 24px;
    padding: 0 0 0 32px;
  }
  .multiselect__content-wrapper{
    border-radius: 8px !important;
    margin-top: 10px;
    border: 1px solid #e8e8e8 !important;
    max-height: 220px !important;
  }
  .multiselect__content-wrapper .multiselect__element .option__desc > span input[type=checkbox]{
    top: 1px;
    position: relative;
  }
  .multiselect__content-wrapper .multiselect__element .option__desc span.option__small{
    margin-left: 10px;
  }
  .multiselect__select{
    height: 48px;
  }
  .multiselect__option{
    min-height: 44px;
  }
  
  .country .multiselect__placeholder {
    padding: 0 0 0 32px !important;
    font-size: 16px !important;
    color: #495057 !important;
    margin-bottom: 8px !important;
  }
  .multiselect__placeholder {
    /* padding: 0 0 0 32px !important; */
    font-size: 16px !important;
    color: #495057 !important;
    margin-bottom: 8px !important;
  }
  .multiselect {
    min-height: 48px;
  }
  .multiselect__spinner {
    height: 46px;
    border-radius: 8px;
  }
  .multiselect--active .multiselect__tags{
    border-color: #B3365B !important;
  }
  .main-filter-section .multiselect__single{
    /* display: none !important; */
    background: #EBCACA !important;
  }

  .form-control:disabled{
     background: #EBCACA !important;
  }
  .multiselect__option--selected.multiselect__option--highlight:after,
  .multiselect__option--selected:after{
    content: '' !important;
  }
  .multiselect--active .icon {
    transform: rotate(180deg);
  }
  .country .multiselect::before{
    content: "\F07D9";
    z-index: 1;
  }
   /* .search-card .multiselect::before{
    content: "\F07D9";
    z-index: 1;
  } */
  .multiselect::before,
  .multiselect--active::after{
    display: inline-block;
    font: normal normal normal 24px/1 "Material Design Icons";
    text-rendering: auto;
    line-height: inherit;
    -webkit-font-smoothing: antialiased;
    position: absolute;
    top: 5px;
    left: 12px;
    font-size: 26px;
  }
  .main-filter-section .multiselect{
    background: #EBCACA;
    border-radius: 8px;
  }
  .main-filter-section .multiselect__tags {
    background: #EBCACA;
  }
  .main-filter-section .multiselect--active .multiselect__tags {
    background: #fff;
  }

  /* dropdown-menu  */
.show-city{
height: 110px;
box-shadow: 0px 2px 8px rgba(40, 41, 61, 0.08), 0px 20px 32px rgba(96, 97, 112, 0.24);    
}

.close-city a{
border-radius: 50% !important;
    padding: 2px 7px !important;
}

.city-list{
height: 110px;
padding: 10px 10px !important;
overflow-y : scroll !important;
overflow-x : hidden !important;
}
.city-list a{
padding: 1px 6px !important;
}

.mdi-check-bold{
    color: rgb(255, 255, 255);
    background: #B3365B;
    border-radius: 100%;
    height: 36px;
    width: 36px;
    padding: 3px 4px;
    font-size: 7px;
}

.close-city {
    /* padding: 0px 5px !important; */
    padding: 0px 5px !important;
    float:right !important;
    float: right !important;
    position: absolute;
    right: 38px;
    bottom: 396px;
}

/* header text */
.header-text-fix{
  margin-top:70px
}

</style>