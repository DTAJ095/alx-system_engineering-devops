#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - runs infinite while loop
 *
 * Return: Void
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates five zombies process
 *
 * Return: Always 0
 */
int main(void)
{
	char count = 0;
	pid_t pid;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID:%d\n", pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
