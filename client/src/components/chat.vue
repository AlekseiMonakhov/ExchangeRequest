<template>
  <div class="root-element">
    <Chat v-if="visible"
          :participants="participants"
          :myself="myself"
          :messages="messageList"
          :chat-title="chatTitle"
          :placeholder="placeholder"
          :colors="colors"
          :border-style="borderStyle"
          :hide-close-button="hideCloseButton"
          :close-button-icon-size="closeButtonIconSize"
          :submit-icon-size="submitIconSize"

          :async-mode="asyncMode"
          :scroll-bottom="scrollBottom"
          :display-header="true"
          :send-images="true"
          :profile-picture-config="profilePictureConfig"
          :timestamp-config="timestampConfig"

          @onMessageSubmit="onMessageSubmit"
       >
    </Chat>
    <div class="element-3">
      <b-button  variant="primary">Согласен с условиями</b-button>
      <b-button  variant="primary">Дата и место обозначены</b-button>
      <b-button  variant="primary">Я получил деньги</b-button>
    </div>
  </div>
</template>

<script>
import {Chat} from 'vue-quick-chat';
import 'vue-quick-chat/dist/vue-quick-chat.css';
import axios from "axios";
import Config from "../../envConfig";

export default {
  components: {
    Chat
  },
  props: {
    deal: {}
  },
  data() {
    return {
      visible: true,
      participants: [
        {
          name: this.isCurrentUser(this.deal.maker_username) ? this.deal.taker_username : this.deal.maker_username,
          id: this.isCurrentUser(this.deal.maker_username) ? this.deal.taker_id : this.deal.maker_id,
        },
      ],
      myself: {
        name: this.isCurrentUser(this.deal.maker_username) ? this.deal.maker_username : this.deal.taker_username,
        id: this.isCurrentUser(this.deal.maker_username) ? this.deal.maker_id : this.deal.taker_id,
      },
      messageList: [],
      chatTitle: `Сделка № ${this.deal.deal_id}`,
      placeholder: 'Отправить сообщение',
      colors: {
        header: {
          bg: '#0080FF',
          text: '#fff'
        },
        message: {
          myself: {
            bg: '#0080FF',
            text: '#fff'
          },
          others: {
            bg: '#fff',
            text: '#0080FF'
          },
          messagesDisplay: {
            bg: '#f7f3f3'
          }
        },
        submitIcon: '#0080FF',
        submitImageIcon: '#0080FF',
      },
      borderStyle: {
        topLeft: "10px",
        topRight: "10px",
        bottomLeft: "10px",
        bottomRight: "10px",
      },
      hideCloseButton: true,
      submitIconSize: 25,
      closeButtonIconSize: "20px",
      asyncMode: false,
      // toLoad: [
      //   {
      //     content: 'Добрый день. Хотел уточнить по заявке',
      //     myself: true,
      //     participantId: 2,
      //     timestamp: {year: 2022, month: 4, day: 10, hour: 10, minute: 10, second: 3, millisecond: 123},
      //     uploaded: true,
      //     viewed: true,
      //     type: 'text'
      //   },
      //   {
      //     content: "Добрый день.  Да, спрашивайте",
      //     myself: false,
      //     participantId: this.deal.taker_id,
      //     timestamp: {year: 2022, month: 4, day: 10, hour: 11, minute: 10, second: 3, millisecond: 123},
      //     uploaded: true,
      //     viewed: false,
      //     type: 'text'
      //   },
      // ],
      scrollBottom: {
        messageSent: true,
        messageReceived: false
      },
      displayHeader:true,
      profilePictureConfig: {
        others: false,
        myself: false,
        styles: {
          width: '30px',
          height: '30px',
          borderRadius: '50%'
        }
      },
      timestampConfig: {
        format: 'dd.MM HH:mm',
        relative: false
      },
    }
  },
  methods: {
    isCurrentUser(username) {
      try {
        const currentUsername = JSON.parse(this.$store.getters.getUser)['username']
        return currentUsername === username
      } catch (e) {
        console.log(e)
      }
    },
    onMessageSubmit: function (message) {
      this.sendMessageToServer({deal_id: this.deal.deal_id, author: JSON.parse(this.$store.getters.getUser)['username'] , type: 'text', content: message.content})
      this.messageList.push(message)
    },
    async sendMessageToServer(data) {
      try {
        await axios.post(`http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/chat/add-messages`, data)
      } catch (e) {
        console.log(e);
      }
    },
    async getMessage() {
      try {
        const messages = await axios.get(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/chat/get-messages/${this.deal.deal_id}`
        );
        if (messages.data && messages.data.length > this.messageList.length ) {
          this.messageList = this.formatToMessageList(messages.data)
        }
      } catch (e) {
        console.log(e);
      }
    },
    formatToMessageList(messages) {
      let messageList = []
      messages.forEach(message => {
        messageList.push({content: message.content, myself: this.isCurrentUser(message.author), participantId: this.isCurrentUser(this.deal.maker_username) ? this.deal.taker_id : this.deal.maker_id, timestamp: message.created_on, uploaded: true, viewed: true, type: message.type})
      })
      return messageList
    },
    //     content: 'Добрый день. Хотел уточнить по заявке',
    //     myself: true,
    //     participantId: 2,
    //     timestamp: {year: 2022, month: 4, day: 10, hour: 10, minute: 10, second: 3, millisecond: 123},
    //     uploaded: true,
    //     viewed: true,
    //     type: 'text'
    // onType: function (event) {
    //   //here you can set any behavior
    // },
    // loadMoreMessages(resolve) {
    //   setTimeout(() => {
    //     resolve(this.toLoad);
    //     this.messages.unshift(...this.toLoad);
    //     this.toLoad = [];
    //   }, 1000);
    // },

    // onClose() {
    //   this.visible = false;
    // },
    // onImageSelected(files, message){
    //   let src = 'https://149364066.v2.pressablecdn.com/wp-content/uploads/2017/03/vue.jpg'
    //   this.messages.push(message);
    //   /**
    //    * This timeout simulates a requisition that uploads the image file to the server.
    //    * It's up to you implement the request and deal with the response in order to
    //    * update the message status and the message URL
    //    */
    //   setTimeout((res) => {
    //     message.uploaded = true
    //     message.src = res.src
    //   }, 3000, {src});
    // },
    // onImageClicked(message){
    //   /**
    //    * This is the callback function that is going to be executed when some image is clicked.
    //    * You can add your code here to do whatever you need with the image clicked. A common situation is to display the image clicked in full screen.
    //    */
    //   console.log('Image clicked', message.src)
    // }
  },
  async mounted() {
    try {
      if (!this.deal) {
        await this.$router.push('/myDeals')
      }
      await this.getMessage();
      setInterval(this.getMessage, 20000)
    } catch (e) {
      console.log(e)
    }
  }
}
</script>

<style >
.root-element {
  margin-top: 20px;
}
.element-3 {
  display: flex;
  justify-content: space-around;
  margin-top: 40px;
}
</style>
