<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="alert alert-danger" role="alert">
        <h4>다음의 오류를 해결하시오.</h4>
        <hr />
        <div v-for="(error, idx) in errors" :key="idx">{{error}}</div>
      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input
          type="text"
          class="form-control"
          id="id"
          placeholder="아이디를 입력하십시오"
          v-model="credentials.username"
        />
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input
          type="password"
          class="form-control"
          id="password"
          placeholder="비밀번호를 입력하십시오"
          v-model="credentials.password"
        />
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import router from "../router";
export default {
  name: "LoginForm",
  data() {
    return {
      credentials: {
        username: "",
        password: ""
      },
      // loading: false,
      errors: []
    };
  },
  computed: {
    loading: function () {
      return this.$store.state.loading
    }
  },
  methods: {
    login() {
      if (this.checkForm()) {
        // this.loading = true;
        // django jwt 를 생성하는 주소로 요청을 보냄
        // 이때 post 요청으로 보내야하며 사용자가 입력한 로그인 정보를 같이 넘겨야 함.
        this.$store.dispatch('startLoading')
        axios
          .post("http://127.0.0.1:8000/api-token-auth/", this.credentials)
          .then(res => {
            // this.$session.start();
            // this.$session.set("jwt", res.data.token);
            this.$store.dispatch('endLoading')
            this.$store.dispatch('login', res.data.token)
            router.push("/")
          })
          .catch(err => {
            // 3. 로그인 실패시 loading의 상태를 다시 false로
            // this.loading = false;
            this.$store.dispatch('endLoading')
            console.log(err);
          });
      } else {
        console.log("로그인 검증 실패");
      }
    },
    checkForm() {
      this.errors = [];
      if (!this.credentials.username) {
        this.errors.push("아이디를 입력하시오.");
      }
      if (this.credentials.password.length < 8) {
        this.errors.push("비밀번호는 8자 이상입니다.");
      }
      if (this.errors.length === 0) {
        return true;
      }
    }
  }
};
</script>

<style>
</style>