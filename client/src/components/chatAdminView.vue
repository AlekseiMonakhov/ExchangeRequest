<template>
  <div class="root-element">
    <Chat v-if="visible"
          :participants="participants"
          :myself="myself"
          :messages="messages"
          :chat-title="chatTitle"
          :placeholder="placeholder"
          :colors="colors"
          :border-style="borderStyle"
          :hide-close-button="hideCloseButton"
          :close-button-icon-size="closeButtonIconSize"
          :submit-icon-size="submitIconSize"
          :load-more-messages="toLoad.length > 0 ? loadMoreMessages : null"
          :async-mode="asyncMode"
          :scroll-bottom="scrollBottom"
          :display-header="true"
          :send-images="true"
          :profile-picture-config="profilePictureConfig"
          :timestamp-config="timestampConfig"
          :accept-image-types="'.png, .jpeg'"
          @onMessageSubmit="onMessageSubmit"
          @onType="onType"
          @onClose="onClose"/>
    <div class="element-3">
    </div>
  </div>
</template>

<script>
import {Chat} from 'vue-quick-chat';
import 'vue-quick-chat/dist/vue-quick-chat.css';

export default {
  components: {
    Chat
  },
  data() {
    return {
      visible: true,
      participants: [
        {
          name: 'Taker ID',
          id: 1,
        },
        {
          name: 'Maker ID',
          id: 2,
        },
      ],
      myself: {
        name: 'ADMIN',
        id: 3,
      },
      messages: [],
      chatTitle: 'Сделка №',
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
      toLoad: [
        {
          content: 'Добрый день. Хотел уточнить по заявке',
          myself: false,
          participantId: 2,
          timestamp: {year: 2022, month: 4, day: 10, hour: 10, minute: 10, second: 3, millisecond: 123},
          uploaded: true,
          viewed: true,
          type: 'text'
        },
        {
          content: "Добрый день.  Да, спрашивайте",
          myself: false,
          participantId: 1,
          timestamp: {year: 2022, month: 4, day: 10, hour: 11, minute: 10, second: 3, millisecond: 123},
          uploaded: true,
          viewed: true,
          type: 'text'
        },
      ],
      scrollBottom: {
        messageSent: true,
        messageReceived: false
      },
      displayHeader:true,
      profilePictureConfig: {
        others: true,
        myself: true,
        styles: {
          width: '30px',
          height: '30px',
          borderRadius: '50%'
        }
      },
      timestampConfig: {
        format: 'HH:mm',
        relative: false
      },
    }
  },
  methods: {
    onType: function (event) {
      //here you can set any behavior
    },
    loadMoreMessages(resolve) {
      setTimeout(() => {
        resolve(this.toLoad);
        this.messages.unshift(...this.toLoad);
        this.toLoad = [];
      }, 1000);
    },
    onMessageSubmit: function (message) {
      this.messages.push(message);

      setTimeout(() => {
        message.uploaded = true
      }, 1000)
    },
    onClose() {
      this.visible = false;
    },
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
