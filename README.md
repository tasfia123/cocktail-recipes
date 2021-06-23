# cocktail-recipes

A cocktail recipe generator that helps the user pick a drink based on inputs (e.g. liquor type, flavor profile, etc.).

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/mnc345/cocktail-recipes) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd cocktail-recipes

Use Anaconda to create and activate a new virtual environment, perhaps called "cocktail-recipes":

```sh
conda create -n cocktail-recipes python=3.8
conda activate cocktail-recipes
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your API key:

    COCKTAIL_API:"________"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means each person who uses our code needs to create their own local ".env" file.



### Email Template Setup

##Installation 
From within an active virtual environment, install the sendgrid package:
pip install sendgrid


Follow [this guide](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md) to:
  1) Sign up for a SendGrid account, and complete the "Single Sender Verification" using an email address of choice (i.e. the `EMAIL_ADDRESS`).
  2) Obtain a SendGrid API Key (i.e. the `SENDGRID_API_KEY`).
  3) Create your own [SendGrid Email Template](https://sendgrid.com/dynamic_templates) and locate the template's unique identifier (i.e. the `SENDGRID_TEMPLATE_ID`).
  4) Configure the email template with this [example test data](/sendgrid/receipt_data.json) and [example "handlebars-flavored" HTML code](/sendgrid/receipt_template.html).

### Credentials Setup

Create a new file called ".env" in the root directory of this repo, then copy the contents below into it, adapting the values to match the `EMAIL_ADDRESS` , `SENDGRID_API_KEY`, and `SENDGRID_TEMPLATE_ID`, obtained in the setup step above.

```sh
# the .env file

EMAIL_ADDRESS="me@example.com"
SENDGRID_API_KEY="abc123"
SENDGRID_TEMPLATE_ID="templ789"
```

### Environment Setup

Setup a virtual environment called something like "emails-env" and from within it install a specific version of the sendgrid package, which we'll use to send the emails:

```sh
conda create emails-env python=3.7 # (first time only)
conda activate emails-env

pip install -r requirements.txt
```

## Usage

Run the cocktail recipe script:

```py
python app/cocktail_recipes.py

When prompted, choose inputs.

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.
