# 단원 6: Kubernetes / 오케스트레이션 (AI 기초 트랙)

> 레포: [I-nkamanda/inka-codyssey](https://github.com/I-nkamanda/inka-codyssey) 폴더 6-1 ~ 6-8

---

## 과제 목록

| 주차 | 폴더 | 주제 | 핵심 개념 |
|:----:|:----:|------|----------|
| 6-1 | `6-1` | 컨테이너 오케스트레이션 입문 | K8s 정의, 아키텍처, 배포판 3종 비교 |
| 6-2 | `6-2` | 서비스 타입 | NodePort vs ClusterIP |
| 6-3 | `6-3` | 명령형 vs 선언형 | Pod/Service 역할, YAML Pod 구조, 포트포워딩 |
| 6-4 | `6-4` | Deployment와 ReplicaSet | 배포 전략, 롤링 업데이트 |
| 6-5 | `6-5` | Minikube 클러스터 | 클러스터 다이어그램, 로컬 K8s 환경 |
| 6-6 | `6-6` | 네트워크 보안 | Pod IP 외부 접근 차단 이유, 포트포워딩 |
| 6-7 | — | (누락) | 레포에서 미발견 |
| 6-8 | `6-8` | 스토리지 | PVC/PV 역할, AccessMode 종류, Volume 타입 |

---

## 상세 내용

### 6-1: 컨테이너 오케스트레이션 입문

Kubernetes의 정의와 필요성을 학습합니다. Master Node(Control Plane)와 Worker Node의 아키텍처를 이해하고, K3s, Minikube, kubeadm 등 배포판 3종을 비교합니다.

### 6-2: 서비스 타입

Kubernetes 서비스의 두 가지 주요 타입인 NodePort와 ClusterIP의 차이를 실습합니다. 외부 트래픽 노출 여부에 따른 선택 기준을 학습합니다.

### 6-3: 명령형 vs 선언형 접근

`kubectl run`(명령형)과 YAML 매니페스트(선언형)의 차이를 실습합니다. Pod와 Service의 역할을 이해하고, YAML로 Pod를 정의하는 구조를 학습합니다. `kubectl port-forward`를 활용한 로컬 접근 방법도 다룹니다.

### 6-4: Deployment와 ReplicaSet

Deployment가 ReplicaSet을 관리하는 구조를 이해합니다. 롤링 업데이트, 스케일링, 롤백 등 배포 전략을 실습합니다.

### 6-5: Minikube 클러스터

Minikube를 활용한 로컬 Kubernetes 클러스터 구성을 실습합니다. 클러스터 다이어그램을 작성하여 각 컴포넌트의 관계를 시각화합니다.

### 6-6: Pod 네트워크 보안

Pod IP가 외부에서 직접 접근할 수 없는 이유(클러스터 내부 네트워크)를 학습합니다. Service와 포트포워딩을 통한 안전한 접근 방법을 실습합니다.

### 6-8: 스토리지 (PVC/PV)

Persistent Volume(PV)과 Persistent Volume Claim(PVC)의 역할과 관계를 학습합니다. ReadWriteOnce, ReadOnlyMany, ReadWriteMany 등 AccessMode 종류와 emptyDir, hostPath, NFS 등 Volume 타입을 비교합니다.

> **참고**: 6-7 폴더는 레포에서 발견되지 않았습니다. 과제 누락 또는 다른 형태로 제출된 것으로 추정됩니다.
