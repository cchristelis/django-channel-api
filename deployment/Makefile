PROJECT_ID := channel-api

SHELL := /bin/bash

# ----------------------------------------------------------------------------
#    P R O D U C T I O N     C O M M A N D S
# ----------------------------------------------------------------------------
default: deploy


deploy:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Bringing up fresh instance "
	@echo "You can access it on http://localhost:61200"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) up -d daphne


build:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) build daphne


kill:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "killing in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) kill daphne
	@docker-compose -p $(PROJECT_ID) kill redis


rm:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) rm daphne
	@docker-compose -p $(PROJECT_ID) rm redis
