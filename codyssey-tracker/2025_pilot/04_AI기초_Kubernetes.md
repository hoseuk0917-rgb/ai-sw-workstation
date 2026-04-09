## 1. 미션 개요

본 단원은 Kubernetes(K8s)를 활용한 컨테이너 오케스트레이션의 핵심 개념과 실질적인 운영 방법을 학습하는 것을 목표로 합니다. 컨테이너 기반 애플리케이션의 배포, 관리, 확장, 복구 자동화를 위한 Kubernetes의 아키텍처, 주요 구성 요소, 그리고 다양한 리소스(Pod, Service, Deployment, ReplicaSet, ConfigMap, Secret, PersistentVolume, PersistentVolumeClaim)의 활용법을 다룹니다. 또한, 명령형(Imperative) 방식과 선언형(Declarative) 방식의 차이를 이해하고, YAML 파일을 통한 리소스 정의 및 관리에 숙달하는 데 중점을 둡니다. Minikube를 활용하여 로컬 환경에 Kubernetes 클러스터를 구축하고 실습함으로써 이론적 지식을 실제 환경에 적용하는 능력을 함양합니다.

## 2. 학습 목표

이 과제를 통해 다음을 달성해야 합니다:

*   **컨테이너 오케스트레이션의 개념 이해**: 컨테이너 오케스트레이션의 필요성과 Kubernetes의 역할을 설명할 수 있습니다.
*   **Kubernetes 아키텍처 이해**: Kubernetes 클러스터의 컨트롤 플레인과 워커 노드 구성 요소를 식별하고 각 역할에 대해 설명할 수 있습니다.
*   **Kubernetes 리소스 활용**: Pod, Service, Deployment, ReplicaSet, ConfigMap, Secret, PersistentVolume, PersistentVolumeClaim 등 주요 Kubernetes 리소스를 이해하고 YAML 파일을 사용하여 정의할 수 있습니다.
*   **명령형/선언형 방식 숙달**: `kubectl run`과 같은 명령형 방식과 YAML 파일을 활용한 `kubectl apply -f` 선언형 방식의 차이를 이해하고 적절히 활용할 수 있습니다.
*   **Service 타입 이해**: ClusterIP, NodePort 등 Kubernetes Service의 다양한 타입을 이해하고 외부 접근을 위해 NodePort Service를 구성할 수 있습니다.
*   **Deployment를 통한 애플리케이션 관리**: Deployment를 사용하여 애플리케이션의 복제본 수를 관리하고 롤링 업데이트의 기본 개념을 이해할 수 있습니다.
*   **Minikube 환경 구축 및 활용**: 로컬 환경에 Minikube 클러스터를 설치하고 `kubectl` 명령어를 사용하여 클러스터를 관리할 수 있습니다.
*   **Pod 네트워크 및 포트 포워딩 이해**: Pod IP의 특성을 이해하고 `kubectl port-forward`를 사용하여 로컬 환경에서 Pod에 접근할 수 있습니다.
*   **영구 스토리지 관리**: PersistentVolume(PV)과 PersistentVolumeClaim(PVC)의 개념을 이해하고 동적 프로비저닝을 통해 스토리지를 할당할 수 있습니다.
*   **환경 설정 및 보안 관리**: ConfigMap과 Secret을 사용하여 애플리케이션의 설정 정보와 민감 데이터를 안전하게 관리할 수 있습니다.

## 3. 기능 요구사항

과제에서 구현/수행해야 하는 구체적인 기능이나 작업은 다음과 같습니다:

*   **Docker Desktop Kubernetes 활성화**: Docker Desktop 환경에서 Kubernetes 기능을 활성화합니다.
*   **명령형 Pod 생성 및 관리**: `kubectl run` 명령어를 사용하여 Nginx Pod를 생성하고 `kubectl get pods`, `kubectl describe pod` 명령어로 상태를 확인합니다.
*   **포트 포워딩**: `kubectl port-forward` 명령어를 사용하여 생성된 Pod의 포트를 로컬 포트에 연결하고 웹 브라우저로 접근을 확인합니다.
*   **선언형 Pod 생성 및 관리**: YAML 파일을 작성하여 Nginx Pod를 선언형 방식으로 생성하고 `kubectl apply -f` 명령어로 클러스터에 적용합니다.
*   **NodePort Service 생성 및 접근**: `kubectl expose` 명령어나 YAML 파일을 사용하여 NodePort 타입의 Service를 생성하고, 할당된 NodePort를 통해 웹 브라우저로 접근을 확인합니다.
*   **Deployment를 통한 Pod 복제본 관리**: `deployment.yaml` 파일을 작성하여 `david` 애플리케이션의 Deployment를 생성하고, `replicas` 설정을 통해 Pod 복제본 수를 3개로 유지합니다.
*   **Deployment 스케일링**: `kubectl scale` 명령어를 사용하여 Deployment의 `replicas` 수를 동적으로 변경하고 Pod 개수 변화를 `watch kubectl get pods` 명령어로 실시간 확인합니다.
*   **Minikube 클러스터 설치 및 시작**: `minikube` 명령어를 사용하여 로컬 환경에 Kubernetes 클러스터를 설치하고 시작합니다.
*   **Minikube 내부 탐색**: `minikube ssh` 명령어를 사용하여 Minikube 내부로 접속하고 `docker ps -a` 명령어로 내부 컨테이너를 확인합니다.
*   **Pod 네트워크 접근 테스트**: Minikube 외부와 내부에서 Pod IP로 `ping` 및 `curl` 명령어를 사용하여 Pod 네트워크 접근성을 테스트합니다.
*   **ConfigMap 및 Secret 생성 및 활용 (간접 포함)**: 학습 자료에는 직접적인 실습은 없으나, 개념적으로 ConfigMap과 Secret의 필요성을 이해하고 YAML 구조를 파악합니다.
*   **PersistentVolumeClaim 생성**: `mysql-pvc.yaml` 및 `wp-pvc.yaml` 파일을 작성하여 PersistentVolumeClaim을 생성하고 `kubectl get pvc`, `kubectl describe pvc` 명령어로 상태를 확인합니다.
*   **리소스 정리**: 실습 완료 후 `kubectl delete` 명령어를 사용하여 생성된 Pod, Service, Deployment, PVC 등의 Kubernetes 리소스를 정리합니다.
*   **Git 버전 관리**: 각 과제 완료 후 변경된 파일을 `git add`, `git commit`, `git push` 명령어를 사용하여 Git 저장소에 커밋하고 푸시합니다.

## 4. 핵심 기술 스택

| 카테고리       | 기술/도구         | 설명                                                               |
| :------------- | :---------------- | :----------------------------------------------------------------- |
| **컨테이너 기술** | Docker            | 애플리케이션을 컨테이너로 패키징하고 실행하는 런타임 환경          |
| **오케스트레이션** | Kubernetes (K8s)  | 컨테이너화된 워크로드를 자동 배포, 스케일링, 관리하는 시스템       |
| **로컬 K8s**   | Minikube          | 로컬 머신에 단일 노드 Kubernetes 클러스터를 실행하는 도구          |
| **K8s CLI**    | `kubectl`         | Kubernetes 클러스터를 제어하는 명령줄 도구                         |
| **설정 파일**  | YAML              | Kubernetes 리소스 정의에 사용되는 데이터 직렬화 언어               |
| **버전 관리**  | Git               | 소스 코드 변경 이력을 추적하고 여러 개발자 간 협업을 돕는 시스템   |
| **네트워크**   | NodePort, ClusterIP | Kubernetes Service 타입 (외부/내부 접근 방식)                      |
| **스토리지**   | PersistentVolume (PV), PersistentVolumeClaim (PVC) | Kubernetes에서 영구 스토리지를 추상화하고 관리하는 리소스 |
| **환경 변수**  | ConfigMap, Secret | 애플리케이션 설정 및 민감 정보를 관리하는 Kubernetes 리소스        |
| **운영체제**   | Linux, Windows (WSL) | 실습 환경 (WSL을 통한 Linux 환경 권장)                             |

## 5. 권장 프로젝트 구조

본 과정은 주로 `kubectl` 명령어를 사용하거나 개별 YAML 파일을 생성하여 실습을 진행하므로, 전체적인 프로젝트 구조보다는 각 과제별 YAML 파일 관리에 중점을 둡니다.

```
.
├── Codyssey/
│   ├── .dockerignore                 # Docker 이미지 빌드 시 제외할 파일 목록
│   ├── deployment.yaml               # david 애플리케이션 Deployment 정의
│   ├── service.yaml                  # david 애플리케이션 Service 정의
│   ├── hellok8s.yaml                 # Nginx Pod 선언형 정의 (예시)
│   ├── mysql-pvc.yaml                # MySQL PersistentVolumeClaim 정의
│   ├── wp-pvc.yaml                   # WordPress PersistentVolumeClaim 정의
│   ├── david_pod_backup.yaml         # david Pod 백업 YAML (명령형 생성 후 백업)
│   └── ...                           # 기타 실습 관련 파일 및 디렉토리
└── README.md                         # 프로젝트 설명
```

**구조 설명:**

*   **`Codyssey/`**: 모든 실습 관련 파일과 YAML 정의를 포함하는 최상위 디렉토리입니다.
*   **`.dockerignore`**: Docker 이미지 빌드 시 불필요한 파일(예: `service.yaml`, `deployment.yaml`)이 이미지에 포함되지 않도록 설정합니다.
*   **`*.yaml` 파일**: Kubernetes 리소스(Pod, Service, Deployment, PVC 등)를 선언형으로 정의하는 파일들입니다. 각 리소스별로 명확한 이름을 부여하여 관리합니다.
*   **`david_pod_backup.yaml`**: `kubectl get pod david -o yaml > david_pod_backup.yaml` 명령어를 통해 생성된 Pod의 YAML 정의 백업 파일입니다.

## 6. 구현 핵심 포인트

### 6.1. 컨테이너 오케스트레이션의 이해

컨테이너 오케스트레이션은 대규모 컨테이너 환경에서 애플리케이션의 배포, 관리, 스케일링, 복구를 자동화하는 기술입니다. Kubernetes는 이 분야의 사실상 표준 도구이며, "내 컴퓨터에선 되는데 서버에선 안 돼요" 문제를 해결하고, 가상 머신보다 가볍고 일관된 실행 환경을 제공합니다.

### 6.2. Kubernetes 아키텍처

Kubernetes 클러스터는 크게 **컨트롤 플레인(Control Plane)**과 **워커 노드(Worker Node)**로 구성됩니다.

*   **컨트롤 플레인**: 클러스터의 전반적인 상태를 관리하고 제어합니다.
    *   **API Server**: 모든 클러스터 통신의 중심점. `kubectl` 명령어를 포함한 모든 외부 요청을 처리합니다.
    *   **Scheduler**: 새로 생성된 Pod를 실행할 적절한 워커 노드를 선택합니다.
    *   **Controller Manager**: 클러스터의 현재 상태를 원하는 상태(Desired State)로 유지하기 위한 컨트롤러들을 실행합니다. (예: ReplicaSet Controller, Deployment Controller)
    *   **etcd**: 클러스터의 모든 설정 데이터와 상태 정보를 저장하는 분산 키-값 저장소입니다.
*   **워커 노드**: 컨테이너화된 애플리케이션(Pod)을 실행하는 물리 또는 가상 머신입니다.
    *   **kubelet**: 각 노드에서 실행되며, Pod의 생명 주기를 관리하고 컨테이너 런타임과 통신하여 컨테이너를 실행합니다.
    *   **kube-proxy**: 클러스터 내부 네트워크 규칙을 관리하고 Service 추상화를 구현하여 네트워크 트래픽을 Pod로 라우팅합니다.
    *   **Container Runtime**: 실제 컨테이너를 실행하는 소프트웨어 (예: containerd, Docker).

### 6.3. 명령형 vs 선언형 방식

Kubernetes 리소스를 생성하고 관리하는 두 가지 주요 방식입니다.

*   **명령형 (Imperative)**: 특정 작업을 즉시 수행하도록 명령합니다. 빠르고 간단한 테스트에 유용합니다.
    ```bash
    # Pod 생성
    kubectl run hellok8s --image=nginx --port=80

    # Service 노출
    kubectl expose pod hellok8s --type=NodePort --port=80 --name=hellok8s-yaml

    # Deployment 스케일링
    kubectl scale deployment david-deployment --replicas=1
    ```
*   **선언형 (Declarative)**: 원하는 최종 상태를 YAML 파일로 정의하고, Kubernetes가 그 상태를 유지하도록 합니다. 버전 관리, 반복 가능성, 협업에 유리합니다.
    ```yaml
    # hellok8s.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: hellok8s-yaml
      labels:
        app: helloworld
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
    ```
    ```bash
    # YAML 파일 적용
    kubectl apply -f hellok8s.yaml
    ```
    **명령형과 선언형 비교:**
    | 구분      | 명령형 (Imperative)             | 선언형 (Declarative)            |
    | :-------- | :------------------------------ | :------------------------------ |
    | 사용 예   | `kubectl run`, `kubectl expose` | `kubectl apply -f`              |
    | 특징      | 즉시 명령 실행                  | YAML 파일 기반 상태 선언        |
    | 장점      | 빠른 테스트 및 단발 작업 용이   | 형상 관리 및 반복 실행 가능     |
    | 단점      | 변경 이력 및 추적 어려움        | 초기 작성이 번거롭고 시간 소요  |

### 6.4. Pod와 Service의 역할

*   **Pod**: Kubernetes에서 배포할 수 있는 가장 작은 단위. 하나 이상의 컨테이너, 스토리지, 네트워크 리소스, 컨테이너 실행 방법을 캡슐화합니다. Pod는 일시적이며, 재시작 시 IP가 변경될 수 있습니다.
    ```yaml
    # Pod YAML 예시
    apiVersion: v1
    kind: Pod
    metadata:
      name: david
      labels:
        app: david
    spec:
      containers:
        - name: david
          image: jonghwan159/david:v1
          ports:
            - containerPort: 80
    ```
*   **Service**: Pod 집합에 대한 안정적인 네트워크 접근을 제공하는 추상화 계층입니다. Pod의 IP가 변경되어도 Service의 IP는 고정되어 있어 클라이언트가 안정적으로 접근할 수 있도록 돕습니다.
    *   **ClusterIP**: 클러스터 내부에서만 접근 가능한 가상 IP를 할당합니다. 주로 백엔드 서비스 간 통신에 사용됩니다.
    *   **NodePort**: 각 워커 노드의 특정 포트를 통해 Service를 외부에 노출합니다. 개발/테스트 환경에서 외부 접근에 유용합니다.
    *   **LoadBalancer**: 클라우드 환경에서 외부 로드 밸런서를 프로비저닝하여 Service를 외부에 노출합니다.
    *   **ExternalName**: CNAME 레코드를 사용하여 외부 서비스에 접근합니다.
    ```yaml
    # NodePort Service YAML 예시
    apiVersion: v1
    kind: Service
    metadata:
      name: david-svc
      labels:
        app: david
    spec:
      type: NodePort
      selector:
        app: david # 'app: david' 레이블을 가진 Pod들을 선택
      ports:
        - protocol: TCP
          port: 80       # Service의 포트
          targetPort: 80 # Pod의 컨테이너 포트
    ```

### 6.5. Deployment와 ReplicaSet

*   **Deployment**: Pod와 ReplicaSet을 관리하는 상위 리소스입니다. 선언된 상태(Desired State)를 유지하며, 롤링 업데이트, 롤백 등의 기능을 제공합니다.
*   **ReplicaSet**: 지정된 수의 Pod 복제본을 항상 실행 상태로 유지하는 역할을 합니다. Deployment는 내부적으로 ReplicaSet을 생성하고 관리합니다.
    ```yaml
    # Deployment YAML 예시
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: david-deployment
      labels:
        app: david
    spec:
      replicas: 3 # Pod 복제본 3개 유지
      selector:
        matchLabels:
          app: david
      template: # Pod 템플릿
        metadata:
          labels:
            app: david
        spec:
          containers:
            - name: david
              image: jonghwan159/david:v1.0
              ports:
                - containerPort: 80
    ```
    **Deployment 스케일링:**
    ```bash
    kubectl scale deployment david-deployment --replicas=1 # Pod 개수를 1개로 줄임
    kubectl scale deployment david-deployment --replicas=3 # Pod 개수를 3개로 늘림
    ```

### 6.6. Minikube 클러스터 구성

Minikube는 로컬 환경에서 단일 노드 Kubernetes 클러스터를 쉽게 실행할 수 있도록 돕는 도구입니다. 개발 및 테스트에 이상적입니다.

**설치 및 시작:**
```bash
# Minikube 설치 (Linux 예시)
curl -LO https://storage.googleapis.com/minikube/releases/v1.22.0/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube version

# kubectl 설치 (Linux 예시)
curl -LO "https://dl.k8s.io/release/v1.22.1/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client

# Minikube 시작 (Docker 드라이버 사용)
minikube start --driver=docker
```
**Minikube 내부 탐색:**
```bash
minikube ssh # Minikube 가상 머신 내부로 SSH 접속
docker ps -a # Minikube 내부에서 실행 중인 Kubernetes 구성 요소 컨테이너 확인
exit         # SSH 접속 종료
```

### 6.7. Pod 네트워크 보안 및 포트 포워딩

*   **Pod IP 접근 제한**: Kubernetes 클러스터의 Pod는 내부 가상 네트워크에 존재하므로, 로컬 PC나 외부 환경에서는 Pod IP로 직접 접근할 수 없습니다. 이는 클러스터 내부의 네트워크 격리 정책 때문입니다.
    ```bash
    # 로컬 PC에서 Pod IP로 curl 시도 (실패 가능)
    curl http://<POD_IP>
    ```
*   **포트 포워딩 (Port Forwarding)**: `kubectl port-forward` 명령어를 사용하면 로컬 PC의 특정 포트를 클러스터 내부의 Pod 포트에 직접 연결할 수 있습니다. 이는 Service를 생성하지 않고도 개발/테스트 목적으로 Pod에 직접 접근할 때 유용합니다.
    ```bash
    # Pod의 80번 포트를 로컬 PC의 8080번 포트로 포워딩
    kubectl port-forward pod/<pod-name> 8080:80
    # 브라우저에서 http://localhost:8080 으로 접속
    ```

### 6.8. ConfigMap과 Secret (개념적 이해)

*   **ConfigMap**: 애플리케이션의 설정 데이터를 키-값 쌍으로 저장하는 데 사용됩니다. 민감하지 않은 일반적인 설정(예: 데이터베이스 호스트, 포트 번호, 환경 변수)을 관리합니다. Pod는 ConfigMap의 데이터를 환경 변수, 커맨드 라인 인수 또는 볼륨 파일로 마운트하여 사용할 수 있습니다.
*   **Secret**: 민감한 데이터(예: 비밀번호, API 키, 토큰)를 저장하는 데 사용됩니다. ConfigMap과 유사하게 키-값 쌍으로 데이터를 저장하지만, Base64로 인코딩되어 저장되며, Pod에 마운트될 때 자동으로 디코딩됩니다. Kubernetes는 Secret 데이터를 암호화하여 저장하고 관리합니다.

### 6.9. 스토리지 (PVC/PV, AccessMode, Volume 타입)

Kubernetes는 컨테이너의 휘발성 특성 때문에 영구적인 데이터 저장을 위해 스토리지를 추상화합니다.

*   **PV (PersistentVolume)**: 클러스터 관리자가 사전에 프로비저닝하거나 동적으로 프로비저닝되는 클러스터 내의 실제 물리적 또는 클라우드 스토리지 리소스입니다. 특정 노드에 종속되지 않습니다.
*   **PVC (PersistentVolumeClaim)**: 사용자가 PV에 대한 스토리지 요구사항(크기, 접근 모드 등)을 요청하는 리소스입니다. PVC는 적절한 PV를 찾아 바인딩됩니다.
    ```yaml
    # PersistentVolumeClaim YAML 예시
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: mysql-pv-claim
      labels:
        app: wordpress
    spec:
      accessModes:
        - ReadWriteOnce # 단일 노드에서 읽기/쓰기 가능
      resources:
        requests:
          storage: 20Gi # 20GB 스토리지 요청
    ```
*   **AccessMode**: PV/PVC가 Pod에 마운트될 때 어떻게 접근할 수 있는지를 정의합니다.
    *   `ReadWriteOnce` (RWO): 단일 노드에서만 읽기/쓰기 가능. 대부분의 경우 사용됩니다.
    *   `ReadOnlyMany` (ROX): 여러 노드에서 동시에 읽기만 가능.
    *   `ReadWriteMany` (RWX): 여러 노드에서 동시에 읽기/쓰기 가능. NFS와 같은 공유 파일 시스템에서 지원됩니다.
*   **Volume 타입**: PV가 사용할 수 있는 다양한 스토리지 백엔드 유형입니다.
    *   `hostPath`: 노드의 파일 시스템 경로를 사용. 개발/테스트용으로, 노드가 사라지면 데이터도 사라집니다.
    *   `nfs`: Network File System을 사용. 여러 Pod가 동시에 접근 가능합니다.
    *   `gcePersistentDisk`, `awsElasticBlockStore`: 클라우드 제공업체의 영구 디스크를 사용합니다.
    *   `emptyDir`: Pod의 수명 주기 동안만 존재하는 임시 디렉토리. Pod가 삭제되면 데이터도 사라집니다.
    *   `local`: 특정 노드에 있는 로컬 디스크를 PV로 사용합니다.

## 7. 트러블슈팅 & 팁

*   **`kubectl` 명령어 오타**: `kubectl` 명령어는 대소문자를 구분하며, 리소스 이름도 정확해야 합니다. `kubectl get pods` 대신 `kubectl get pod`도 가능하지만 일관된 사용이 좋습니다.
*   **YAML 파일 문법 오류**: YAML은 들여쓰기가 매우 중요합니다. 스페이스 2칸 또는 4칸을 일관되게 사용해야 하며, 탭 문자는 사용하지 않습니다. YAML 유효성 검사기(예: `https://codebeautify.org/yaml-validator`)를 활용하세요.
*   **Pod `Pending` 상태**: Pod가 `Pending` 상태에 머무는 경우, 스케줄러가 Pod를 배치할 노드를 찾지 못했거나, 필요한 리소스(CPU, 메모리, 볼륨)가 부족할 수 있습니다. `kubectl describe pod <pod-name>` 명령어로 이벤트를 확인하여 원인을 파악합니다.
*   **Pod `CrashLoopBackOff` 상태**: 컨테이너가 계속 시작되었다가 종료되는 상태입니다. 애플리케이션 코드 오류, 잘못된 설정, 컨테이너 이미지 문제 등이 원인일 수 있습니다. `kubectl logs <pod-name>` 명령어로 컨테이너 로그를 확인합니다.
*   **Service `Pending` 상태 (LoadBalancer)**: 클라우드 환경에서 LoadBalancer Service를 생성했을 때 `Pending` 상태에 머무는 경우, 클라우드 제공업체의 로드 밸런서 프로비저닝에 실패했거나 권한 문제가 있을 수 있습니다. Minikube에서는 `NodePort`를 주로 사용합니다.
*   **Minikube 시작 오류**: `minikube start` 시 오류가 발생하면, `minikube delete`로 클러스터를 완전히 삭제한 후 다시 시작해 보세요. Docker 데몬이 실행 중인지 확인하고, 필요한 경우 Docker Desktop 설정을 확인합니다.
*   **`kubectl port-forward` 터미널 점유**: `kubectl port-forward`는 명령을 실행한 터미널을 점유합니다. 다른 `kubectl` 명령어를 사용하려면 새 터미널을 열어야 합니다. 백그라운드 실행을 원한다면 `&`를 붙이거나 `nohup`을 사용할 수 있습니다.
*   **`.dockerignore` 활용**: Docker 이미지 빌드 시 `service.yaml`, `deployment.yaml`과 같은 Kubernetes 설정 파일은 이미지에 포함될 필요가 없습니다. `.dockerignore` 파일에 해당 파일들을 추가하여 이미지 크기를 줄이고 보안을 강화합니다.
    ```
    # .dockerignore 예시
    service.yaml
    deployment.yaml
    ```
*   **`kubectl get all` 활용**: 실습 후 클러스터의 모든 리소스(Pod, Service, Deployment, ReplicaSet 등) 상태를 한눈에 확인하려면 `kubectl get all` 명령어를 사용합니다. PV, PVC까지 확인하려면 `kubectl get all,pv,pvc`를 사용합니다.
*   **`watch` 명령어**: `watch kubectl get pods`와 같이 `watch` 명령어를 사용하면 특정 명령어의 출력을 주기적으로 갱신하여 실시간으로 상태 변화를 모니터링할 수 있습니다. 이는 Deployment 스케일링과 같이 동적인 변화를 관찰할 때 매우 유용합니다.

## 8. 추가 학습 자료

*   **Kubernetes 공식 문서 (한글)**:
    *   [Kubernetes 개념](https://kubernetes.io/ko/docs/concepts/)
    *   [kubectl 명령어 치트 시트](https://kubernetes.io/ko/docs/reference/kubectl/cheatsheet/)
    *   [Pod 라이프사이클](https://kubernetes.io/ko/docs/concepts/workloads/pods/pod-lifecycle/)
    *   [Service](https://kubernetes.io/ko/docs/concepts/services-networking/service/)
    *   [Deployment](https://kubernetes.io/ko/docs/concepts/workloads/controllers/deployment/)
    *   [Persistent Volumes](https://kubernetes.io/ko/docs/concepts/storage/persistent-volumes/)
    *   [ConfigMap](https://kubernetes.io/ko/docs/concepts/configuration/configmap/)
    *   [Secret](https://kubernetes.io/ko/docs/concepts/configuration/secret/)
*   **Minikube 공식 문서**:
    *   [Minikube 시작하기](https://minikube.sigs.k8s.io/docs/start/)
*   **Docker 공식 문서**:
    *   [Docker 개요](https://docs.docker.com/get-started/overview/)
*   **YAML 문법 검사기**:
    *   [Code Beautify YAML Validator](https://codebeautify.org/yaml-validator)
    *   [YAML to JSON Converter](https://codebeautify.org/yaml-to-json-xml-csv)