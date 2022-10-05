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
      container: null,
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
      scrollBottom: {
        messageSent: true,
        messageReceived: true
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
