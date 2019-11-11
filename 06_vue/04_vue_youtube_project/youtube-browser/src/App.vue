<template>
  <div id="App">
    <!-- 만약 inputChange 이벤트가 일어나면 onInputChange라는 메서드 실행 됌 -->
    <search-bar @inputChange="onInputChange"></search-bar>
    <div class="row">
      <video-detail :video="selectedVideo"></video-detail>
      <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
    </div>
    <!-- 왼쪽: props (가변) 오른쪽: 현재 위치 키값(match) -->
  </div>
</template>

<script>
import axios from "axios";
import SearchBar from "./components/SearchBar";
import VideoList from "./components/VideoList";
import VideoDetail from "./components/VideoDetail";

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;
const API_URL = "https://www.googleapis.com/youtube/v3/search";

export default {
  name: "App", // 최상단 컴포넌트 --- 이름이 없어도 되지만 명시적으로 작성
  data() {
    return {
      videos: [],
      selectedVideo: null
    };
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail
  },
  methods: {
    onVideoSelect(video) {
      this.selectedVideo = video;
    },
    onInputChange(inputValue) {
      axios
        .get(API_URL, {
          params: {
            key: API_KEY,
            type: "video",
            part: "snippet",
            q: inputValue
          }
        })
        .then(response => {
          this.videos = response.data.items;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style>
</style>
