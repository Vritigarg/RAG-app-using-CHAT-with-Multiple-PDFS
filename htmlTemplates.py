css = '''
<style>
.chat-message{
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user{
    background-color: #2b313e
}
.chat-message.bot{
    background-color: #475063
}
.chat-message .avatar{
    width: 20%;
}
.chat-message .avatar img{
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message{
    width: 80%;
    padding: 0.15rem;
    color: #fff;
}
'''

bot_template = '''
<div class = "chat-message bot">
    <div class = "avatar">
        <img src = "https://i.ibb.co/qWBwpNb/Photo-logo-5.png">
    <div>
    <div class = "message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class = "chat-message user">
    <div class = "avatar">
        <img src = "https://t4.ftcdn.net/jpg/09/43/48/93/360_F_943489384_zq3u5kkefFjPY3liE6t81KrX8W3lvxSz.jpg">
    <div>
    <div class = "message">{{MSG}}</div>
</div>
'''
