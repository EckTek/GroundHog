##
## EPITECH PROJECT, 2020
## CNA_groundhog_2019
## File description:
## Makefile
##

SRC			=	src/main.py

NAME		=	groundhog

TEST_NAME	=	execTest

all:	$(NAME)

$(NAME):
	@rm -f $(NAME)
	@touch $(NAME) && chmod +x $(NAME)
	-cat $(SRC) > $(NAME)

graph:

clean:
	-rm -r __pycache__


fclean:	clean
	rm -f $(NAME)
	rm -f $(TEST_NAME)


re:	fclean all


.PHONY:	clean fclean re all
