<template>
  <b-navbar toggleable="lg" type="dark" class="pr-4">
    <b-navbar-brand class="text-white" href="#">Logipsum</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto py-2">
        <b-nav-item href="#">How it works</b-nav-item>
        <b-nav-item href="#">Solutions</b-nav-item>
        <b-nav-item href="#">Contact</b-nav-item>
      </b-navbar-nav >
    </b-collapse>
  </b-navbar>
</template>

<script>
  export default {

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
    color: #fff !important;
  }
  .nav-item:nth-child(2){
    margin-left: 44px;
    margin-right: 44px;
  }
  nav.navbar{
    position: absolute;
    width: 100%;
  }
  .navbar-collapse.collapse.show .nav-item a{
    color: #000 !important;
    text-align: right;
    padding: 10px 15px;
  }
  .navbar-collapse.collapse.show{
    background: #fff;
    z-index: 1;
    border-radius: 5px;
  }

  @media only screen and (max-width: 1000px) {
 .nav-item:nth-child(2){
    
    margin-right: 0px;
  }
}

</style>