# Co.Lab-CT-Software-Dev.-Assess.
Code Challenge Overview Welcome to the Co.Lab Software development program code challenge! This challenge is designed to assess your ability to build a simple web page that meets specific requirements. You have the freedom, flexibility and creativity to use whatever language or framework you’d like to complete the challenge.

We suggest spending no more than 4-5 hours on this assessment.
Project Description
Create and deploy a simple web application that follows the following requirements:
Your web app must include a short bio about you and your professional history.
Your web app should display a few of your side projects or professional projects and should include a link to access the projects.
Your web app should make an API call to display 3-5 pieces of data you retrieve from the API service. You are welcome to choose whatever API you’d like to use.
Include a section to explain why you chose the specific API you used in your project.
Your web app should be designed using brand colors from the Co.Lab site. Please reference our website and see how we structure information and how buttons and links are designed.
Your web app must be mobile-responsive.
Lastly, you must also deploy and host your web app using any service of your choice. (e.g. Netlify, Vercel, etc.)
Remember to be as creative as possible with your solution. This is your time to shine, and let us know the kind of engineer you are. We want your work to speak for you.
Sample Project
Please check out the sample project below. While this is an example, we don’t expect you to copy the exact implementation. It’s just a benchmark for what we would expect from you. Its the time to show your skills and be creative with your solution to build what is unique.
Co.Lab Dev Assessment 1
Submission
You’ll have one week to complete this assessment.
Once you have completed the project, please use the following form to submit the URL of your web app:
[Submission form link] 
We will contact you in a few days after evaluating your project.
The next step after this will be an interview with someone on the Career Partnerships team.
After the interview, if you’re the right fit, we’ll send you an offer to join the cohort of your choice.
Evaluation
Your submission will be evaluated based on the following criteria:
Completion of all requirements.
Creativity in design and layout.
Content included in your project





















<!DOCTYPE html>
<html>
<head>
    <title>Your Web App</title>
    <!--<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">-->
    <link rel="stylesheet" href="static/ style.css">
</head>


<body>

    <div id="bio-section">
        <h1>About Me</h1>
        <p>Your bio and professional history goes here.</p>
    </div>

    <div id="projects-section">
        <h1>Projects</h1>
        <!-- Project links -->
    </div>

        <!-- API data goes here -->
    <div id="api-section">
        <h1>API Data</h1>
        <p>Todo: {{ api_data.title }}</p>
    </div>
    
    <div id="database-section">
        <h1>Database Version</h1>
        <p>Connected to PostgreSQL version: 13.11 (Ubuntu 13.11-1.pgdg20.04+1) {{ version }}</p>
    </div>
    
</body>
</html>

















<!DOCTYPE html>
<html>
<head>
    <title>Co.Lab-CT-Assess.</title>
    <!--<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">--->
    <link rel="stylesheet" href="static/ style.css">
</head>
</head>
<body>

    <!-- Top Navigation Bar -->
    <div class="navbar">
        <span>Co.Lab <> CT Software Development Assessment</span>
    </div>
    
    <!-- Main Content -->
    <div style="margin-top: 60px;"> <!-- To avoid overlap with the fixed navbar -->
        
        <div id="bio-section">
            <div>
                <button class="button1"><h1>About Me</h1></button>
            </div>

            <div>
                <button class="button2"><i>I grew up on the central coast of California, from Santa Cruz to Carmel, from the mellow waves at Pleasure Point to the forest mountain trails of Big Sur.</i></button>
            </div>

            <div>
                <button class="button3"><i>In Software/Tech for nearly 20 years, from Digital Products at a community newspaper, to Business Development for Series D SF startup, now in Growth Consultant role for AI/ML software enterprise</i></button>
            </div>

    

        </div>
    
        <div id="projects-section">
            <h1>Projects</h1>
            <div class="container">
                <div class="grid-item">Item 1</div>
                <div class="grid-item">Item 2</div>
                <div class="grid-item">Item 3</div>
                <!-- Add more items here -->
            </div>
            <!-- Project links -->
        </div>
    
        <!-- API data goes here -->
        <div id="api-section">
            <h1>API Data</h1>
            <p>Todo: {{ api_data.title }}</p>
        </div>

        <!-- Grid Container -->
        <div class="container">
            <div class="grid-item">Item 1</div>
            <div class="grid-item">Item 2</div>
            <div class="grid-item">Item 3</div>
            <!-- Add more items here -->
        </div>
    
        <!-- Buttons -->
        <div>
            <button class="button">Click Me</button>
        </div>

        <div id="database-section">
            <h1>Database Version:</h1>
            <p>Connected to PostgreSQL version: 13.11 (Ubuntu 13.11-1.pgdg20.04+1) {{ version }}</p>
        </div>
    
    </div>
</body>
</html>






