from BBC.AWS.CloudFormation.Common.Component import Component

component = Component("thomap12-cosmos-training")
component.set_health_check_url("/status")
component.render()
