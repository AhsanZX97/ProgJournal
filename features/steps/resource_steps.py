from behave import when,given,then


@given(u'i\'m on the home page')
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000")


@when(u'I click on the add resource button')
def step_impl(context):
    button = context.browser.find_element_by_id('add')
    button.click()


@when(u'I fill out the form')
def step_impl(context):
    name = context.browser.find_element_by_xpath('/html/body/form/input[2]')
    name.send_keys('Google')
    url = context.browser.find_element_by_xpath('/html/body/form/input[3]')
    url.send_keys('www.google.com')


@when(u'Click Submit')
def step_impl(context):
    submit = context.browser.find_element_by_id('submit')
    submit.click()


@then(u'I should see the resource added to the home page')
def step_impl(context):
    result = context.browser.find_element_by_class_name('Google')
    assert 'Google' == result.text