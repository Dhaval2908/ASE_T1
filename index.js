const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();

app.set('view engine', 'ejs'); // Set EJS as the view engine
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('static'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.post('/predict', (req, res) => {
    const formData = req.body;
    const pythonProcess = spawn('python', ['predict.py', JSON.stringify(formData)]);

    pythonProcess.stdout.on('data', (data) => {
        const predictions = JSON.parse(data);
        res.render('result', { alert: predictions[0], description: predictions[1] }); // Render 'result' template
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
