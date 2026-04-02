FROM nginx:alpine
LABEL org.opencontainers.image.title="my-custom-nginx"
LABEL org.opencontainers.image.description="AI/SW 개발 워크스테이션 과제용 정적 웹 서버"
COPY app/ /usr/share/nginx/html/
