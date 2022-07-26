<template>

    <beautiful-chat
      :participants="participants"
      :onMessageWasSent="onMessageWasSent"
      :messageList="messageList"
      :newMessagesCount="newMessagesCount"
      :isOpen="isChatOpen"
      :close="closeChat"
      :open="openChat"
      :showFile="true"
      :showEdition="true"
      :showDeletion="true"
      :showTypingIndicator="showTypingIndicator"
      :showLauncher="true"
      :showCloseButton="true"
      :colors="colors"
      :alwaysScrollToBottom="alwaysScrollToBottom"
      :messageStyling="messageStyling"
      @onType="handleOnType"
      @edit="editMessage"/>
</template>
<script>
import { Chat } from 'vue-beautiful-chat'
export default {
  components: {Chat},
  props: {

  },
  data() {
    return {
      participants: [
        {
          id: 'user1',
          name: 'Mahuhuh',
        },
        {
          id: 'user2',
          name: 'Suppohhrt',
        }
      ], // the list of all the participant of the conversation. `name` is the user name, `id` is used to establish the author of a message, `imageUrl` is supposed to be the user avatar.

      messageList: [
        {type: 'text', author: `me`, data: {text: `Say yes!`}},
        {type: 'text', author: `user1`, data: {text: `No.`}}
      ], // the list of the messages to show, can be paginated and adjusted dynamically
      newMessagesCount: 0,
      isChatOpen: false, // to determine whether the chat window should be open or closed
      showTypingIndicator: '', // when set to a value matching the participant.id it shows the typing indicator for the specific user
      colors: {
        header: {
          bg: '#4e8cff',
          text: '#ffffff'
        },
        launcher: {
          bg: '#4e8cff'
        },
        messageList: {
          bg: '#ffffff'
        },
        sentMessage: {
          bg: '#4e8cff',
          text: '#ffffff'
        },
        receivedMessage: {
          bg: '#eaeaea',
          text: '#222222'
        },
        userInput: {
          bg: '#f4f7f9',
          text: '#565867'
        }
      }, // specifies the color scheme for the component
      alwaysScrollToBottom: true, // when set to true always scrolls the chat to the bottom when new events are in (new message, user starts typing...)
      messageStyling: true // enables *bold* /emph/ _underline_ and such (more info at github.com/mattezza/msgdown)
    }
  },
  methods: {
    sendMessage(text) {
      if (text.length > 0) {
        this.newMessagesCount = this.isChatOpen ? this.newMessagesCount : this.newMessagesCount + 1
        this.onMessageWasSent({author: 'support', type: 'text', data: {text}})
      }
    },
    onMessageWasSent(message) {
// called when the user sends a message
      this.messageList = [...this.messageList, message]
    },
    openChat() {
// called when the user clicks on the fab button to open the chat
      this.isChatOpen = true
      this.newMessagesCount = 0
    },
    closeChat() {
// called when the user clicks on the botton to close the chat
      this.isChatOpen = false
    },
    handleScrollToTop() {
// called when the user scrolls message list to top
// leverage pagination for loading another page of messages
    },
    handleOnType() {
      console.log('Emit typing event')
    },
    editMessage(message) {
      const m = this.messageList.find(m => m.id === message.id);
      m.isEdited = true;
      m.data.text = message.data.text;
    }
  }
}
</script>


<!--<template>-->
<!--  <div class="root-element">-->
<!--    <Chat v-if="visible"-->
<!--          :participants="participants"-->
<!--          :myself="myself"-->
<!--          :messages="messages"-->
<!--          :chat-title="chatTitle"-->
<!--          :placeholder="placeholder"-->
<!--          :colors="colors"-->
<!--          :border-style="borderStyle"-->
<!--          :hide-close-button="hideCloseButton"-->
<!--          :close-button-icon-size="closeButtonIconSize"-->
<!--          :submit-icon-size="submitIconSize"-->
<!--          :load-more-messages="toLoad.length > 0 ? loadMoreMessages : null"-->
<!--          :async-mode="asyncMode"-->
<!--          :scroll-bottom="scrollBottom"-->
<!--          :display-header="true"-->
<!--          :send-images="true"-->
<!--          :profile-picture-config="profilePictureConfig"-->
<!--          :timestamp-config="timestampConfig"-->
<!--          @onImageClicked="onImageClicked"-->
<!--          @onImageSelected="onImageSelected"-->
<!--          @onMessageSubmit="onMessageSubmit"-->
<!--          @onType="onType"-->
<!--          @onClose="onClose">-->
<!--    </Chat>-->
<!--    <div class="element-3">-->
<!--      <b-button  variant="primary">Согласен с условиями</b-button>-->
<!--      <b-button  variant="primary">Дата и место обозначены</b-button>-->
<!--      <b-button  variant="primary">Я получил деньги</b-button>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import {Chat} from 'vue-quick-chat';-->
<!--import 'vue-quick-chat/dist/vue-quick-chat.css';-->

<!--export default {-->
<!--  components: {-->
<!--    Chat-->
<!--  },-->
<!--  data() {-->
<!--    return {-->
<!--      visible: true,-->
<!--      participants: [-->
<!--        {-->
<!--          name: 'Maker ID',-->
<!--          id: 1,-->
<!--        },-->
<!--      ],-->
<!--      myself: {-->
<!--        name: 'Taker ID',-->
<!--        id: 2,-->
<!--      },-->
<!--      messages: [],-->
<!--      chatTitle: 'Сделка №',-->
<!--      placeholder: 'Отправить сообщение',-->
<!--      colors: {-->
<!--        header: {-->
<!--          bg: '#0080FF',-->
<!--          text: '#fff'-->
<!--        },-->
<!--        message: {-->
<!--          myself: {-->
<!--            bg: '#0080FF',-->
<!--            text: '#fff'-->
<!--          },-->
<!--          others: {-->
<!--            bg: '#fff',-->
<!--            text: '#0080FF'-->
<!--          },-->
<!--          messagesDisplay: {-->
<!--            bg: '#f7f3f3'-->
<!--          }-->
<!--        },-->
<!--        submitIcon: '#0080FF',-->
<!--        submitImageIcon: '#0080FF',-->
<!--      },-->
<!--      borderStyle: {-->
<!--        topLeft: "10px",-->
<!--        topRight: "10px",-->
<!--        bottomLeft: "10px",-->
<!--        bottomRight: "10px",-->
<!--      },-->
<!--      hideCloseButton: true,-->
<!--      submitIconSize: 25,-->
<!--      closeButtonIconSize: "20px",-->
<!--      asyncMode: false,-->
<!--      toLoad: [-->
<!--        {-->
<!--          content: 'Добрый день. Хотел уточнить по заявке',-->

<!--          participantId: 2,-->
<!--          timestamp: {year: 2022, month: 4, day: 10, hour: 10, minute: 10, second: 3, millisecond: 123},-->
<!--          uploaded: true,-->
<!--          viewed: true,-->
<!--          type: 'text'-->
<!--        },-->
<!--        {-->
<!--          content: "Добрый день.  Да, спрашивайте",-->

<!--          participantId: 1,-->
<!--          timestamp: {year: 2022, month: 4, day: 10, hour: 11, minute: 10, second: 3, millisecond: 123},-->
<!--          uploaded: true,-->
<!--          viewed: false,-->
<!--          type: 'text'-->
<!--        },-->
<!--      ],-->
<!--      scrollBottom: {-->
<!--        messageSent: true,-->
<!--        messageReceived: false-->
<!--      },-->
<!--      displayHeader:true,-->
<!--      profilePictureConfig: {-->
<!--        others: false,-->
<!--        myself: false,-->
<!--        styles: {-->
<!--          width: '30px',-->
<!--          height: '30px',-->
<!--          borderRadius: '50%'-->
<!--        }-->
<!--      },-->
<!--      timestampConfig: {-->
<!--        format: 'HH:mm',-->
<!--        relative: false-->
<!--      },-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    onType: function (event) {-->
<!--      //here you can set any behavior-->
<!--    },-->
<!--    loadMoreMessages(resolve) {-->
<!--      setTimeout(() => {-->
<!--        resolve(this.toLoad);-->
<!--        this.messages.unshift(...this.toLoad);-->
<!--        this.toLoad = [];-->
<!--      }, 1000);-->
<!--    },-->
<!--    onMessageSubmit: function (message) {-->
<!--      this.messages.push(message);-->

<!--      setTimeout(() => {-->
<!--        message.uploaded = true-->
<!--      }, 1000)-->
<!--    },-->
<!--    onClose() {-->
<!--      this.visible = false;-->
<!--    },-->
<!--    onImageSelected(files, message){-->
<!--      let src = 'https://149364066.v2.pressablecdn.com/wp-content/uploads/2017/03/vue.jpg'-->
<!--      this.messages.push(message);-->
<!--      /**-->
<!--       * This timeout simulates a requisition that uploads the image file to the server.-->
<!--       * It's up to you implement the request and deal with the response in order to-->
<!--       * update the message status and the message URL-->
<!--       */-->
<!--      setTimeout((res) => {-->
<!--        message.uploaded = true-->
<!--        message.src = res.src-->
<!--      }, 3000, {src});-->
<!--    },-->
<!--    onImageClicked(message){-->
<!--      /**-->
<!--       * This is the callback function that is going to be executed when some image is clicked.-->
<!--       * You can add your code here to do whatever you need with the image clicked. A common situation is to display the image clicked in full screen.-->
<!--       */-->
<!--      console.log('Image clicked', message.src)-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style >-->

<!--.root-element {-->
<!--  margin-top: 20px;-->
<!--}-->

<!--.element-3 {-->
<!--  display: flex;-->
<!--  justify-content: space-around;-->
<!--  margin-top: 40px;-->
<!--}-->

<!--</style>-->
