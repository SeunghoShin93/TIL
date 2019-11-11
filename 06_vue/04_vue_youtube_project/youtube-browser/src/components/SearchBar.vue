<template>
  <div>
    <input @change="onInput" type="text" />
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  methods: {
    onInput(e) {
      this.$emit("inputChange", e.target.value);
      //console.log(e.target.value);
    }
  }
};
</script>

<style scoped>
input {
  width: 70%;
}

div {
  text-align: center;
  margin: 20px;
}
</style>