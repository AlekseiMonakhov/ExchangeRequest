module.exports = {
  apps: [{
    name: "client",
    script: "npm run dev",
    watch: true,
  },{
    name: "server",
    script: "cd ../server/; python3 app.py",
    watch: true
  }]
}
