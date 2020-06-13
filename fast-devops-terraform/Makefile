all:

dev:
	ls *.tf | entr -c terraform plan -out=beer.tfplan

update:
	terraform plan -out=beer.tfplan
	terraform apply beer.tfplan

updatev:
	TF_LOG=DEBUG make update