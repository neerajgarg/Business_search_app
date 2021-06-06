<template>
  <div>
    <b-overlay
      :show="isSearching"
      variant="transparent"
      opacity="0.5"
      blur="1rem"
      rounded="sm"
      v-if="isSearching"
    >
    </b-overlay>
    <nav
      class="navbar navbar-expand-lg fixed-top"
      :class="scrollPosition < 50 ? 'is-transparent' : 'is-bg-light'"
    >
      <div class="container">
        <a class="navbar-brand" href="#">LOGO</a>
        <button
          class="navbar-toggler btn-transparent"
          type="button"
          data-toggle="collapse"
          data-target="#mainNavbar"
          aria-controls="mainNavbar"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="mdi mdi-menu"></span>
        </button>

        <div class="collapse navbar-collapse" id="mainNavbar">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#"
                >Home <span class="sr-only">(current)</span></a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Pricing</a>
            </li>
            <li class="nav-item">
              <a class="btn btn-custom-outlined" href="#">contact us</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="header custom-bg">
      <div class="container">
        <div class="row justify-content-between align-items-center">
          <div class="col-md-7 my-2">
            <h1 class="header-title is-invert">
              Find Organisations <br />
              That Suits Your Work
            </h1>
            <p class="header-content is-invert">Work!!</p>
            <a href="" class="btn-custom">know more</a>
          </div>

          <div class="col-md-5 my-2">
            <div class="card">
              <div class="card-body">
                <h3 class="card-title">Search Organisations For Your Work</h3>
                <div class="my-3">
                  <a
                    @click="type = 'keyword'"
                    class="card-tab-btn"
                    :class="{ active: type == 'keyword' }"
                    >by keywords</a
                  >
                  <a
                    @click="type = 'job'"
                    class="card-tab-btn"
                    :class="{ active: type == 'job' }"
                    >by job titles</a
                  >
                </div>

                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <div class="input-group-text">
                      <span class="mdi mdi-magnify"></span>
                    </div>
                  </div>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="search by keywords"
                    v-model="keyword"
                  />
                </div>

                <div class="input-group mb-2">
                  <div class="input-group-prepend">
                    <div class="input-group-text">
                      <span class="mdi mdi-map-marker"></span>
                    </div>
                    <div class="input-group-text label">Location</div>
                  </div>
                  <b-form-select
                    v-model="country"
                    class="text-capitalize form-control"
                    :options="countries"
                  ></b-form-select>
                </div>

                <div class="form-group">
                  <label>Score: 0-{{ sliderVal }} </label>
                  <!-- <div id="custom-slider">
                    <input type="hidden" value="50" id="slider" tabindex="-1" />
                    <div id="selector"></div>
                    <div id="progressBar"></div>
                  </div> -->
                  <div class="slider-wrapper">
                    <div class="slider-track"></div>
                    <div class="slider-controller" tabindex="-1">
                      <div
                        class="slider"
                        tabindex="0"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        aria-valuenow="40"
                        aria-valuetext="40"
                        :style="{ left: sliderPos }"
                      ></div>
                      <div
                        class="slider-range"
                        :style="{ width: sliderPos }"
                      ></div>
                    </div>
                    <input
                      type="range"
                      :min="sliderMin"
                      :max="sliderMax"
                      id="slider-input"
                      tabindex="-1"
                      v-model="sliderVal"
                    />
                  </div>
                </div>
                <button
                  class="btn btn-primary-color btn-block"
                  @click="search"
                  :disabled="keyword.trim() == ''"
                >
                  search
                </button>
                <div
                  class="d-flex"
                  id="popular-searches"
                  v-if="keywords.length > 0"
                >
                  <span class="is-light">Popular searches: </span>
                  <span>
                    <span v-for="(keyword, i) in keywords" :key="i">
                      <a @click="search_keyord(keyword)">{{ keyword }}</a>
                      &nbsp;
                    </span>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <section v-if="isSearchDone" class="results" id="results">
      <div class="container">
        <div class="d-flex justify-content-between align-items-center">
          <h1 class="section-header">Results</h1>
          <div class="views">
            <span
              class="mdi mdi-view-grid"
              :class="{ active: view == 'grid' }"
              @click="view = 'grid'"
            ></span>
            <span
              class="mdi mdi-view-list"
              :class="{ active: view == 'list' }"
              @click="view = 'list'"
            ></span>
          </div>
          <button
            type="button"
            class="btn btn-transparent d-md-none"
            @click="showModal = true"
          >
            <span class="mdi mdi-filter"></span>
          </button>

          <b-modal v-model="showModal" :busy="true" centered>
            <template>
              <div class="d-flex justify-content-between align-items-center">
                <h6 class="card-title">Filters</h6>
                <button
                  class="btn btn-sm btn-primary-color"
                  @click="applyFilter"
                >
                  apply
                </button>
              </div>
            </template>
            <template>
              <div class="form-group">
                <select id="page_pl" class="form-control" v-model="rpp">
                  <option value="50">50</option>
                  <option value="80">80</option>
                  <option value="100">100</option>
                </select>
              </div>
              <!-- <div class="form-group">
                    <label for="inputState">Job Title</label>
                    <b-form-select
                  v-model="city"
                  class="text-capitalize form-control"
                  :options="cities"
                  @change="searchByCity"
                ></b-form-select>
                  </div> -->
                  
              <div class="form-group">
                <label for="inputState">State</label>
                <b-form-select
                  v-model="state"
                  class="text-capitalize form-control"
                  :options="states"
                  @change="searchByState"
                ></b-form-select>
              </div>
              <div class="form-group">
                <label for="inputState">City</label>
                <b-form-select
                  v-model="city"
                  class="text-capitalize form-control"
                  :options="cities"
                  @change="searchByCity"
                ></b-form-select>
              </div>
              <div class="form-group">
                <label for="inputState">Company Size</label>
                <select id="size" class="form-control" v-model="employee">
                  <option value="any" selected>any</option>
                  <option value="1-99">1-99</option>
                  <option value="100-249">100-249</option>
                  <option value="250-499">250-499</option>
                  <option value="500-999">500-999</option>
                  <option value="1000-4999">1000-4999</option>
                  <option value="5000-9000">5000-9999</option>
                  <option value="10000-10000000">10000+</option>
                </select>
                <!-- <b-form-select
                  v-model="employee"
                  class="text-capitalize form-control w-100"
                  :options="emps"
                  @change="searchBySize"
                ></b-form-select> -->
              </div>
            </template>
          </b-modal>
        </div>

        <div
          class="d-md-flex justify-content-between align-items-center d-none"
        >
          <div
            class="d-flex align-items-center justify-content-end"
            id="filters"
          >
            <!-- <h5 class="mt-3">Filters:</h5> -->
            <div class="form-row">
              <!-- <div class="form-group col-md-3">
                <label for="inputState">Job Title</label>
                <select id="job_title" class="form-control">
                  <option selected>any</option>
                  <option>web developer</option>
                </select>
              </div> -->
              <div class="form-group col-md-3">
                <label for="inputState">Pages per load</label>
                <select
                  id="page_pl"
                  class="form-control"
                  v-model="rpp"
                  @change="searchBySize"
                >
                  <option value="50">50</option>
                  <option value="80">80</option>
                  <option value="100">100</option>
                </select>
              </div>
              <div class="form-group col-md-3">
                <label for="inputState">State</label>
                <b-form-select
                  v-model="state"
                  class="text-capitalize form-control w-100"
                  :options="states"
                  @change="searchByState"
                ></b-form-select>
              </div>
              <div class="form-group col-md-3">
                <label for="inputState">City</label>
                <b-form-select
                  v-model="city"
                  class="text-capitalize form-control w-100"
                  :options="cities"
                  @change="searchByCity"
                ></b-form-select>
              </div>
              <div class="form-group col-md-3">
                <label for="inputState">Company Size</label>
                <select
                  id="size"
                  class="form-control w-100"
                  v-model="employee"
                  @change="searchBySize"
                >
                  <option value="any" selected>any</option>
                  <option value="1-99">1-99</option>
                  <option value="100-249">100-249</option>
                  <option value="250-499">250-499</option>
                  <option value="500-999">500-999</option>
                  <option value="1000-4999">1000-4999</option>
                  <option value="5000-9000">5000-9999</option>
                  <option value="10000-10000000">10000+</option>
                </select>
                <!-- <b-form-select
                  v-model="employee"
                  class="text-capitalize form-control w-100"
                  :options="emps"
                  @change="searchBySize"
                ></b-form-select> -->
              </div>
            </div>
          </div>
        </div>

        <div class="d-flex d-md-none justify-content-end" id="color-codes">
          <div class="d-flex align-items-center m-2">
            <span class="box bg-critical"></span>
            <p class="text-critical">Critical</p>
          </div>
          <div class="d-flex align-items-center m-2">
            <span class="box bg-good"></span>
            <p class="text-good">Good</p>
          </div>
          <div class="d-flex align-items-center m-2">
            <span class="box bg-recommanded"></span>
            <p class="text-recommanded">Recommended</p>
          </div>
        </div>

        <div
          class="row justify-content-between my-4"
          v-if="companies.length > 0"
        >
          <div
            class="results"
            :class="view == 'list' ? 'col-md-10' : 'col-md-12'"
          >
            <div class="row align-items-stretch mx-0">
              <div
                class="flip-card col-12"
                :class="[
                  company.class,
                  view == 'list'
                    ? 'result-list-card px-0'
                    : 'result-grid-card col-md-4 my-2',
                ]"
                id="card-1"
                v-for="(company, i) in companies"
                :key="company.id"
              >
                <div
                  :class="
                    flips.includes(i)
                      ? 'flip-card-inner flip'
                      : 'flip-card-inner'
                  "
                >
                  <div class="flip-card-front">
                    <div class="result-score" v-bind:class="getClass(company.score)">
                      <h1 v-if="company.score > 75">75</h1>
                      <h1 v-else>{{ parseInt(company.score) }}</h1>
                      <h5>score</h5>
                    </div>
                    <div class="result-content">
                      <div class="result-subtitle">
                        <h5>{{ company.industry }}</h5>
                      </div>
                      <div class="result-title">
                        <h3>{{ company.company_name }}</h3>
                      </div>
                      <div class="result-info">
                        <small>
                          <span class="mdi mdi-account mr-2"> </span>
                          <span>
                            {{ company.salutation }} {{ company.first_name }}
                            {{ company.last_name }},<span class="is-light mx-1">
                              ( {{ company.job_level }} )</span
                            ></span
                          >
                        </small>
                        <small>
                          <span class="mdi mdi-office-building mr-2"> </span>
                          {{ company.job_title }}
                        </small>
                        <small>
                          <span class="mdi mdi-account-group mr-2"> </span>
                          {{ company.employees }} employees
                        </small>
                        <small>
                          <span class="mdi mdi-home-map-marker mr-2"> </span>
                          {{ company.address }}
                        </small>
                      </div>
                      <a class="show-more" @click="toggleFlip(i)">show more</a>
                    </div>
                  </div>
                  <div class="flip-card-back">
                    <div class="result-content">
                      <div class="subscribe" v-if="!company.hasAdditionalData">
                        <a href="" class="subs-btn">subscribe</a>
                        <p class="is-light">
                          This part is only available for members
                        </p>
                      </div>
                      <div class="result-info" v-else>
                        <!-- <small v-if="company.emp_role !== ''">
                          <span class="mdi mdi-chess-knight mr-2"> </span>
                          {{ company.emp_role }}
                        </small> -->
                        <small v-if="company.email !== ''">
                          <span class="mdi mdi-email mr-2"> </span>
                          {{ company.email }}
                        </small>
                        <small v-if="company.phone !== ''">
                          <span class="mdi mdi-phone mr-2"> </span>
                          {{ company.phone }}
                        </small>

                        <!-- <small v-if="company.emp_addr !== ''">
                          <span class="mdi mdi-map-marker-radius mr-2"> </span>
                          {{ company.emp_addr }}
                        </small>
                        <small v-if="company.emp_linkedin !== ''">
                          <span class="mdi mdi-linkedin mr-2"> </span>
                          {{ company.emp_linkedin }}
                        </small>

                        <small v-if="company.company_phone !== ''">
                          <span class="mdi mdi-deskphone mr-2"> </span>
                          {{ company.company_phone }}
                        </small> -->
                        <small v-if="company.revenue !== ''">
                          <span class="mdi mdi-trending-up mr-2"> </span>
                          {{ company.revenue }}
                        </small>
                        <small v-if="company.campaign !== ''">
                          <span class="mdi mdi-star mr-2"> </span>
                          {{ company.campaign }}
                        </small>
                        <small v-if="company.tag_line !== ''">
                          <span class="mdi mdi-label-variant mr-2"> </span>
                          {{ company.tag_line }}
                        </small>
                      </div>
                      <a class="show-more" @click="toggleFlip(i)">show less</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div
            class="col-md-2 d-none d-md-block color-codes"
            v-if="view == 'list'"
          >
            <div class="ml-auto mr-0 fit-content">
              <h5>Color codes</h5>
              <div class="d-flex align-items-center my-2">
                <span class="box bg-critical"></span>
                <p class="text-critical">Critical</p>
              </div>
              <div class="d-flex align-items-center my-2">
                <span class="box bg-good"></span>
                <p class="text-good">Good</p>
              </div>
              <div class="d-flex align-items-center my-2">
                <span class="box bg-recommanded"></span>
                <p class="text-recommanded">Recommanded</p>
              </div>
            </div>
          </div>
        </div>

        <div class="row justify-content-center my-5 py-5" v-else>
          <h4 class="text-center">No data found</h4>
        </div>

        <button
          @click="fetchMore"
          class="btn btn-primary-color btn-block w-25 mx-auto"
          v-if="hasEqualSize"
        >
          show more
        </button>
      </div>
    </section>

    <section v-if="popular.length > 0">
      <!-- <section> -->
      <div class="container">
        <h3 class="section-subheader text-center">
          Most viewed organisation for
        </h3>
        <h1 class="section-header text-center">{{ keyword }}</h1>
        <hr class="hr" />

        <div class="row align-items-stretch mx-0">
          <div
            class="flip-card result-grid-card col-md-4 my-2"
            v-for="(company, i) in popular"
            :key="company.id"
          >
            <div
              :class="
                popflips.includes(i)
                  ? 'flip-card-inner flip'
                  : 'flip-card-inner'
              "
            >
              <div class="flip-card-front">
                <div class="result-score">
                  <h1 v-if="parseInt(company.score) > 75">75</h1>
                  <h1 v-else>{{ parseInt(company.score) }}</h1>
                  <h5>score</h5>
                </div>
                <div class="result-content">
                  <div class="result-subtitle">
                    <h5>{{ company.industry }}</h5>
                  </div>
                  <div class="result-title">
                    <h3>{{ company.company_name }}</h3>
                  </div>
                  <div class="result-info">
                    <small>
                      <span class="mdi mdi-account mr-2"> </span>
                      <span>
                        {{ company.salutation }} {{ company.first_name }}
                        {{ company.last_name }},<span class="is-light mx-1">
                          ( {{ company.job_level }} )</span
                        ></span
                      >
                    </small>
                    <small>
                      <span class="mdi mdi-office-building mr-2"> </span>
                      {{ company.job_title }}
                    </small>
                    <small>
                      <span class="mdi mdi-account-group mr-2"> </span>
                      {{ company.employees }} employees
                    </small>
                    <small>
                      <span class="mdi mdi-map-marker mr-2"> </span>
                      {{ company.address }}
                    </small>
                  </div>
                  <a class="show-more" @click="togglePopFlip(i)">show more</a>
                </div>
              </div>
              <div class="flip-card-back">
                <div class="result-content">
                  <div class="result-info">
                    <div class="subscribe" v-if="!isSubscribed">
                      <a href="" class="subs-btn">subscribe</a>
                      <p class="is-light">
                        This part is only available for members
                      </p>
                    </div>
                    <div v-if="isSubscribed">
                      <small>
                        <span class="mdi mdi-email mr-2"> </span>
                        {{ company.email }}
                      </small>
                      <small>
                        <span class="mdi mdi-phone mr-2"> </span>
                        {{ company.phone }}
                      </small>
                      <small>
                        <span class="mdi mdi-trending-up mr-2"> </span>
                        {{ company.revenue }}
                      </small>
                      <small>
                        <span class="mdi mdi-star mr-2"> </span>
                        {{ company.campaign }}
                      </small>
                      <small>
                        <span class="mdi mdi-label-variant mr-2"> </span>
                        {{ company.tag_line }}
                      </small>
                    </div>
                  </div>
                  <a class="show-more" @click="togglePopFlip(i)">show less</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- <div class="fixed-left">
      <form id="subscriber-form">
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="isSubscribe"
            id="exampleRadios1"
            value="false"
            checked
            v-model="isSubscribed"
          />
          <label class="form-check-label" for="exampleRadios1">
            guest
          </label>
        </div>
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="isSubscribe"
            id="exampleRadios2"
            value="true"
            v-model="isSubscribed"
          />
          <label class="form-check-label" for="exampleRadios2">
            subscriber
          </label>
        </div>
      </form>
    </div> -->
  </div>
</template>

<script>
import constants from "../api/constants";
var VueScrollTo = require("vue-scrollto");

export default {
  data() {
    return {
      showModal: false,
      isSearching: false,

      scrollPosition: 0,
      view: "list",
      sliderMin: 0,
      sliderMax: 100,
      sliderVal: 80,
      sliderPos: null,
      isSearchDone: false,
      hasEqualSize: false,
      isSubscribed: false,

      countries: constants.COUNTRIES,
      states: ["any"],
      cities: ["any"],
      emps: ["any"],
      companies: [],
      popular: [],
      keywords: [],
      flips: [],
      popflips: [],
      last_id: null,

      type: "keyword",
      rpp: 15,
      country: "any",
      state: "any",
      city: "any",
      keyword: "",
      employee: "any",
    };
  },
  created() {
    this.getKeywords();
    this.updateValues();
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
      this.isSearchDone = true;
      this.isSearching = true;

      let params = {
        score: this.sliderVal,
        limit: this.rpp,
        keyword: this.keyword,
        search_type: this.type,
        country: this.country !== "any" ? this.country : "",
        state: this.state !== "any" ? this.state : "",
        city: this.city !== "any" ? this.city : "",
        employee: this.employee !== "any" ? this.employee : "1-10000000",
        isFirstSearch: true,
      };

      const res = await this.$axios.$get("/search", { params });
      console.log(res)

      if (res.status == 'sucess') {
        if (res.data.length > 0) {
          this.last_id = res.data[res.data.length - 1].id;
        }
        this.companies = res.data;
      }

      params = {
        keyword: this.keyword,
        search_type: this.type,
      };

      this.isSearching = false;
      VueScrollTo.scrollTo("#results", 200, { offset: -50 });

      const popularResult = await this.$axios.$get("/popular", { params });
      console.log(popularResult)

      if (popularResult.status == 'sucess') {
        this.popular = popularResult.data;
      }

      if (this.country == "any") {
        const states = await this.$axios.$get("/states");

        const cities = await this.$axios.$get("/cities");

        this.states = states.data;
        this.cities = cities.data;
      } else {
        let params = { country: this.country };

        const states = await this.$axios.$get("/states", { params });

        const cities = await this.$axios.$get("/cities", { params });

        this.states = states.data;
        this.cities = cities.data;
      }

      this.hasEqualSize = res.data.length == this.rpp ? true : false;
    },

    async searchBySize() {
      this.isSearching = true;

      const res = await this.$axios.$get("/search", {
        params: {
          score: this.sliderVal,
          limit: this.rpp,
          keyword: this.keyword,
          search_type: this.type,
          country: this.country !== "any" ? this.country : "",
          state: this.state !== "any" ? this.state : "",
          city: this.city !== "any" ? this.city : "",
          employee: this.employee !== "any" ? this.employee : "1-10000000",
        },
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
      this.isSearching = true;

      const res = await this.$axios.$get("/search", {
        params: {
          score: this.sliderVal,
          limit: this.rpp,
          keyword: this.keyword,
          search_type: this.type,
          state: this.state !== "any" ? this.state : "",
          employee: this.employee !== "any" ? this.employee : "1-10000000",
        },
      });

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
      this.cities.push("any");

      this.city = "any";

      this.hasEqualSize = res.data.length == this.rpp ? true : false;
      this.isSearching = false;
    },

    async searchByCity() {
      this.isSearching = true;

      const res = await this.$axios.$get("/search", {
        params: {
          score: this.sliderVal,
          limit: this.rpp,
          keyword: this.keyword,
          search_type: this.type,
          state: this.state !== "any" ? this.state : "",
          city: this.city !== "any" ? this.city : "",
          employee: this.employee !== "any" ? this.employee : "1-10000000",
        },
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

    async fetchMore() {
      this.isSearching = true;

      const res = await this.$axios.$get("/search", {
        params: {
          lId: this.last_id,
          score: this.sliderVal,
          limit: this.rpp,
          keyword: this.keyword,
          search_type: this.type,
          country: this.country !== "any" ? this.country : "",
          state: this.state !== "any" ? this.state : "",
          city: this.city !== "any" ? this.city : "",
          employee: this.employee !== "any" ? this.employee : "1-10000000",
        },
      });

      if (res.status == 'sucess') {
        console.log(res.data);
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
};
</script>
