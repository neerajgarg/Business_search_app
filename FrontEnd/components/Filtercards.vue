<template>
  <div class="container" id="results" v-if="companies && companies.length > 0">
    <div class="row">
        <div class="col-md-4" v-for="company, index  in companies" :key="index">
          <div class="filter-custom-card">
            <div class="row custom-card-header align-items-center clearfix m-0">
              <div class="company-details float-left">
                <p class="company-name mb-0">
                  {{ company.industry }}
                </p>
                <p    class="company-details mb-0">
                  {{ company.company_name }}
                </p>
              </div>
              <!-- <div class="float-right" :class="company.score < 31 ? 'score-red': company.score > 30 && company.score < 51 ? 'score-yellow' : 'score'" >
                <div class="" :class="company.score < 31 ? 'score-red': company.score > 30 && company.score < 51 ? 'score-yellow' : 'score'" >
                  {{ company.score }}
                </div>
              </div> -->
            </div>
            <div class="custom-card-content text-left">
                <div class="mb-3 employee-title-section">
                    <p class="employee-name mb-0">{{ company.salutation }} {{ company.first_name }}
                            {{ company.last_name }}
                    </p>
                    <p   class="employee-position mb-0">
                       {{ company.job_level }}
                    </p>
                </div>
                <div class="employee-details-section">
                    <p  v-if="!flippedCards.includes(index)"  class="mb-0 emp-list-item"><span class="mdi mdi-account mr-2">
                      </span> {{ company.job_level }}
                    </p>
                    
                    <p  v-if="!flippedCards.includes(index)"  class="mb-0 emp-list-item">
                      <span class="mdi mdi-account-multiple mr-2"></span> {{ company.employees }} 
                    </p>

                    <p  v-if="!flippedCards.includes(index)" class="mb-0 emp-list-item">
                      <span class="mdi mdi-map-marker mr-2 "></span> {{ company.address }} 
                    </p>

                    <p  v-if="isSubscribed && flippedCards.includes(index)" class="mb-0 emp-list-item">
                      <span class="mdi mdi-phone mr-2"></span>  {{ company.phone }} 
                    </p>
                    
                    <p  v-if="isSubscribed && flippedCards.includes(index)" class="mb-0 emp-list-item">
                      <span class="mdi mdi-trending-up mr-2"></span>  {{ company.revenue }} 
                    </p>
                    
                    <p  v-if="isSubscribed && flippedCards.includes(index)" class="mb-0 emp-list-item">
                      <span class="mdi mdi-star mr-2"></span> {{ company.campaign }} 
                    </p>
                    
                    <p  v-if="isSubscribed && flippedCards.includes(index)" class="mb-0 emp-list-item">
                      <span class="mdi mdi-email mr-2"></span> {{ company.email }} 
                    </p>

                    <p  v-if="isSubscribed && flippedCards.includes(index)" class="mb-0 emp-list-item">
                      <span class="mdi mdi-label-variant mr-2"></span> {{ company.tag_line }} 
                    </p>

                    <p  v-if="!isSubscribed && flippedCards.includes(index)" class="mb-0 emp-list-item">
                      <span class="mdi mdi-name"></span>  This part is only available for members 
                    </p>
                </div>
            </div>
            <div class="text-right">
              <span  @click="togglePopFlip(index)"  class="show-more-less">
                  <span v-if="!flippedCards.includes(index)">Show more</span>
                  <span v-else>Show less</span>
              </span>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  props: ['companies'],
  data(){
    return {
      flippedCards:[],
      isSubscribed:true
    }
  },

  methods: {
    togglePopFlip(index){
      if(this.flippedCards.includes(index)){
        const pos = this.flippedCards.indexOf(index);
        console.log(pos)
          if (pos > -1) {
            this.flippedCards.splice(pos, 1);
          }
      }else{
         this.flippedCards.push(index)
      }

  }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.company-name{
  font-size: 14px;
  font-weight: 400;
  line-height: 18px;
  text-align: left;
  color: #031C32;
}

.score-red{
  background: #D22237;
  color: white;
  border-radius: 40px;
  font-size: 24px;
  font-style: normal;
  font-weight: 300;
  line-height: 26px;
  letter-spacing: 0em;
  text-align: center;
  padding: 10px;
}

.score-yellow{
  background: #DF772C;
  color: black;
  border-radius: 40px;
  font-size: 24px;
  font-style: normal;
  font-weight: 300;
  line-height: 26px;
  letter-spacing: 0em;
  text-align: center;
  padding: 10px;
}

.company-details{
  font-size: 16px;
  font-weight: 700;
  line-height: 20px;
  text-align: left;
  color: #031C32;
  width: 73%;
  max-height: 56px;
  min-height: 56px;
}
.filter-custom-card{
  background: #EBCACA;
  border-radius: 8px;
  margin-bottom: 30px;
}
.custom-card-header{
  background: #D9B9BA;
  border-radius: 8px 8px 0px 0px;
  padding: 16px;
}
.score{
  background: #0C7A85;
  border-radius: 40px;
  color: white;
  font-size: 24px;
  font-style: normal;
  font-weight: 300;
  line-height: 26px;
  letter-spacing: 0em;
  text-align: center;
  padding: 10px;
}
.employee-name{
  color: #B3365B;
  font-weight: 700;
  font-size: 18px;
  line-height: 23px;
}
.employee-position{
  font-weight: normal;
  font-size: 14px;
  line-height: 18px;
  color: #031C32;
}
.custom-card-content{
    padding: 16px;
}
.employee-details-section{
  min-height: 80px;
  max-height: 120px;
}
.employee-title-section{
  min-height: 41px;
}
.emp-list-item{
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 18px;
  letter-spacing: 0em;
  text-align: left;
  color: #031C32;
}
.show-more-less{
  font-size: 14px;
  font-style: normal;
  font-weight: 700;
  line-height: 18px;
  letter-spacing: 0em;
  text-align: right;
  padding: 0 16px 16px 16px;
  display: inline-block;
}
.show-more-less span{
    cursor: pointer;
}
</style>
