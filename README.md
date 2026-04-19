# 🧠 AI Document Assistant (RAG System)

A production-style Retrieval-Augmented Generation (RAG) system built with **FastAPI, ChromaDB, PostgreSQL, and Sentence-Transformers**.  
This project enables users to upload documents and ask intelligent questions over their content using LLM-powered retrieval.

---

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Intelligent text chunking
- 🧠 Embedding generation using Sentence Transformers
- 📦 Vector storage using ChromaDB
- 🔍 Semantic search (RAG pipeline)
- 🤖 LLM-based response generation (pluggable: OpenAI / Gemini / local models)
- 🐳 Fully Dockerized environment
- 🗄 PostgreSQL integration for scalable backend extension

---

## 🏗️ System Architecture

```text
User
 ↓
FastAPI Backend
 ↓
Document Ingestion Pipeline
 (PDF → Text → Chunking)
 ↓
Embedding Model (Sentence-Transformers)
 ↓
ChromaDB (Vector Store)
 ↓
Retriever (Top-K Similar Chunks)
 ↓
LLM (Response Generation)
 ↓
User
