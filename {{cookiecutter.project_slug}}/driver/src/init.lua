{%- set driver_name = cookiecutter.project_name | slugify(separator="_") %}
local log = require "log"
local capabilities = require "st.capabilities"
local Driver = require "st.Driver"

local function handle_a(driver, device, command)
    log.info("Send <A> command to device")
end

local function handle_b(driver, device, command)
    log.info("Send <B> command to device")
end

-- Driver library initialization
local {{driver_name}} =
    Driver("{{driver_name}}",
        {
            capability_handers = {
                -- TODO create a handler for each capability:command
                [capabilities.XXX.ID] =
                {
                    [capabilities.XXX.commands.CMDa.NAME] = handle_a,
                    [capabilities.XXX.commands.CMDb.NAME] = handle_b
                }
            }
        }

-- Run the driver
{{driver_name}}:run()