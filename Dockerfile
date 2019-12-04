FROM amazonlinux

RUN cd ~ \
    && yum install git golang make python -y \
    && git clone https://github.com/Lujie1996/fasthttp.git \
    && cd fasthttp/examples/fileserver \
    && make \
    && rm -rvf static \
    && python generate_files.py

EXPOSE 80 81 82 83 84

ENTRYPOINT [ "./root/fasthttp/examples/fileserver/fileserver", "-addr=0.0.0.0:80", "-dir=/root/fasthttp/examples/fileserver/static"]
