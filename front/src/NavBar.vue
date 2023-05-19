<template>
  <header>
    <nav class="navbar navbar-expand-sm navbar-light bg-light">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand"> <b>MOV;GO</b> </router-link>

        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link to="/" class="nav-link">HOME</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'movies' }" class="nav-link"
              >MOVIES</router-link
            >
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'ego' }" class="nav-link"
              >EGO</router-link
            >
          </li>
          <li class="nav-item">
            <router-link to="/login" class="nav-link">LOGIN</router-link>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
// import { mapGetters } from "vuex";
export default {
  name: "NavBar",
  data() {
    return {};
  },
  methods: {
    // logout() {
    //   this.$store.dispatch("logout");
    // },
  },
  computed: {
    // ...mapGetters(["isLoggedIn"]),
    // loginState() {
    //   return this.isLoggedIn ? "Logout" : "Login";
    // },
  },
};
</script>

<style scoped></style>
