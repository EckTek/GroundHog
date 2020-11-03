##
## EPITECH PROJECT, 2020
## CNA_groundhog_2019
## File description:
## Makefile
##

SRC			=	src/main.py

T_SRC		=	test/main.py

NAME		=	groundhog

TEST_NAME	=	execTest

all:	$(NAME)

$(NAME):
	@rm -f $(NAME)
	@touch $(NAME) && chmod +x $(NAME)
	-cat $(SRC) > $(NAME)

debug:	$(TEST_NAME)

$(TEST_NAME):
	rm -f $(TEST_NAME)
	@touch $(TEST_NAME) && chmod +x $(TEST_NAME)
	-cat $(T_SRC) > $(TEST_NAME)

clean:
	@-rm -r __pycache__
	@-rm -r src/__pycache__
	@-rm -r test/__pycache__
	@-rm -f *~


fclean:	clean
	rm -f $(NAME)
	rm -f $(TEST_NAME)


re:	fclean all

test: fclean debug

.PHONY:	clean fclean re all