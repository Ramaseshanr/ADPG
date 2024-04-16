#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *read_file(const char *filename)
{
  size_t bytes_read = 0;

  FILE *fp = fopen(filename, "r");
  if (fp == NULL)
  {
    printf("Couldn't open file %s\n", filename);
    return NULL;
  }

  fseek(fp, 0, SEEK_END);
  long size = ftell(fp);
  fseek(fp, 0, SEEK_SET);

  char *content;
  if (size != -1)
  {
    content = (char*)malloc(size + 1);
    if (content == NULL)
    {
      fclose(fp);
      return NULL;
    }
  }
  else
  {
    // Handle unknown file size (reallocate dynamically)
    content = (char*)malloc(1024); // Initial allocation
    if (content == NULL)
    {
      fclose(fp);
      return NULL;
    }
    size_t allocated_size = 1024;
    while ((bytes_read = fread(content + bytes_read, 1, allocated_size - bytes_read, fp)) > 0)
    {
      if (bytes_read == allocated_size - bytes_read)
      { // Buffer full, reallocate
        allocated_size *= 2;
        content = (char*)realloc(content, allocated_size);
        if (content == NULL)
        {
          fclose(fp);
          return NULL;
        }
      }
    }
    content[bytes_read] = '\0';
  }

  if (fread(content, 1, size != -1 ? size : bytes_read, fp) != (size != -1 ? size : bytes_read))
  {
    free(content);
    fclose(fp);
    return NULL;
  }

  fclose(fp);

  return content;
}

void free_file_content(char *content)
{
  if (content != NULL)
  {
    free(content);
  }
}