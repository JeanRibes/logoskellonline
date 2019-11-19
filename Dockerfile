#très mal fait, il faudrait Gunicorn/uswgi...
FROM haskell as builder
COPY compiler.hs /
RUN ghc /compiler.hs -o /compiler

FROM python:3.7
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
COPY --from=builder /compiler .
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
