FROM python:3.13.5-slim-bookworm

ENV PYTHONDONTWRITEBYTECOE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

WORKDIR /app

RUN apt-get update && apt-get install -y curl

#COPY --from=ghcr.io/astral-sh/uv:python3.13-bookworm-slim /uv /uvx /bin/
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY requirements.txt .
RUN uv pip install -r requirements.txt --system

# Install GNU Gettext tools for makemessages and compilemessages
RUN apt-get install -y gettext

#RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["./entrypoint.sh"]